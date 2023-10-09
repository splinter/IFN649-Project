import threading
import time
import logging
from clients.commands import fetch_commands,update_command
from network.commands import get_input_commands_queue, get_output_commands_queue
from network.device import heartbeat_device

commandPollingInterval=10
heartbeat=60*5

def poll_server_for_commands():
    inQ = get_input_commands_queue()
    while True:
        commands = fetch_commands()
        if len(commands) > 0:
            inQ.put(commands)
        time.sleep(commandPollingInterval)
    return

def push_update_commands():
    outQ = get_output_commands_queue()

    while True:
        commandStatus = outQ.get()
        result = update_command(deviceID="", commandID=commandStatus.deviceID, status=commandStatus.status)
        if result is True:
            logging.info("Successfully updated command status")
    return

def update_plant_info():
    return

def send_hearbeat():
    while True:
        heartbeat_device()
        time.sleep(heartbeat)
    return

def start():

    commands=threading.Thread(target=poll_server_for_commands)
    commandsUpdate = threading.Thread(target=push_update_commands)

    device= threading.Thread(target=send_hearbeat)
    
    commands.start()
    logging.info("Started thread to fetch new commands")
    commandsUpdate.start()
    logging.info("Started thread to update commands")
    device.start()
    return

start()
