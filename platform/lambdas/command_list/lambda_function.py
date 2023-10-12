import logging
import json
from table_clients.commands import list_commands

def get_device_id(event):
    query = event["queryStringParameters"]
    return query["deviceID"]

def lambda_handler(event,context):
    deviceID = get_device_id(event)    
    commands = list_commands(deviceID)
    return {
        "status": "success",
        "data": commands
    }