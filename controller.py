import threading
import time
import logging
from clients.commands import fetch_commands,update_command
from network.commands import get_input_commands_queue, get_output_commands_queue
from network.device import heartbeat_device
from network.edge import start_communication_with_arduino
from scheduling.commands import Scheduler
from telemtry.sensor import SensorTelemetry

commandPollingInterval=10
heartbeat=60*5

def poll_server_for_commands(scheduler ):
    inQ = get_input_commands_queue()
    while True:
        commands = fetch_commands()
        if len(commands) > 0:
            scheduler.register_command(commands)
            for command in commands:
                inQ.put(command)
        time.sleep(commandPollingInterval)
    return

def push_update_commands():
    outQ = get_output_commands_queue()

    while True:
        commandStatus = outQ.get()
        result = update_command(deviceID="", commandID=commandStatus.commandID, status=commandStatus.status)
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
    scheduler= Scheduler()
    commands=threading.Thread(target=poll_server_for_commands,args=[scheduler])
    commandsUpdate = threading.Thread(target=push_update_commands)

    arduino=threading.Thread(target=heartbeat_device)

    deviceHeartbeat= threading.Thread(target=send_hearbeat)


    schedulerThread= threading.Thread(target=scheduler.schedule)
    schedulerThread.start()
    
    commands.start()
    logging.info("Started thread to fetch new commands")
    commandsUpdate.start()
    logging.info("Started thread to update commands")
    deviceHeartbeat.start()
    start_communication_with_arduino()
    return

start()
