import json
from table_clients.commands import Command, update_command_status

def get_command(event):
    bodyStr = event["body"]
    body = {}
    body = json.loads(bodyStr)
    commandID = body["commandID"]
    deviceID = body["deviceID"]
    status = body["status"]
    command = Command()
    command.commandID=commandID
    command.deviceID = deviceID
    command.status = status
    return command

def lambda_handler(event,context):
    command = get_command(event)
    status = update_command_status(command)
    return {
        "status": "success"
    }
