import logging
import json
import uuid
from table_clients.commands import create_command,Command

def get_command(event):
    bodyStr = event["body"]
    body = {}
    body = json.loads(bodyStr)
    command = Command()
    command.commandID = str(uuid.uuid4())
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
