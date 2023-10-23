import threading
import time
import serial
import queue
import logging
from network.commands import get_input_commands_queue,update_commands

port = "/dev/rfcomm0"
baudrate = 9600
sendCommandQueue= queue.Queue()
recievedDataQueue = queue.Queue()

def recieve_teensy(ser):
    data = ser.readline()
    m = data.decode("utf-8").strip("\r\n")
    print(m)
    recievedDataQueue.put(m)
    return

def recieve_network_updates():
    inQueue = get_input_commands_queue()
    while True:
        command = inQueue.get()
        sendCommandQueue.put(command)
    return

def recieve_serial_updates():
    try:
        ser = serial.Serial(port,9600)
    except Exception:
        logging.error("Unable to create serial connection with teensy board.")
        return

    while True:
        if ser.in_waiting:
            recieve_teensy(ser)
        if sendCommandQueue.not_empty:
            command = sendCommandQueue.get()
            logging.info("Sending command " + command)
            ser.write(str.encode(command+"\r\n"))
        time.sleep(5)

def process_serial_updates():
    while True:
        data = recievedDataQueue.get()
        time.sleep()

def start_communication_with_arduino():
    serialThread = threading.Thread(target=recieve_serial_updates)
    commandsThread = threading.Thread(target=recieve_network_updates)
    serialThread.start()
    commandsThread.start()
    while True:
        time.sleep(1)
    return
