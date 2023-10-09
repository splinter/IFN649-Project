import logging
import json
from table_clients.commands import create_command,Command

def get_command(event):
    bodyStr = event.body
    body = {}
    body = json.load(bodyStr)
    command = Command()
    command.deviceID=body["deviceID"]
    command.plantId=body["plantID"]
    command.code = body["code"]
    return command

def lambda_handler(event,context):
    print(event)
    command = get_command(event)
    result = create_command(command)
    return {
        "status": "success"
    }
