import threading
import time
from commands import get_input_commands_queue,update_commands

def send_command_to_device(command):
    return True

def recieve_network_updates():
    inQueue = get_input_commands_queue()
    while True:
        command = inQueue.get()
        send_command_to_device(command)
    return

def recieve_serial_updates():
    
    while True:
        time.sleep()

def process_serial_updates():
    while True:
        time.sleep()

def start_communication_with_arduino():
    return