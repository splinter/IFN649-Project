import boto3
import time

client = boto3.client("dynamodb")
TABLE_NAME = "IOT-Commands"

COMMAND_STATUS_INIT = "init"
COMMAND_STATUS_SENT_TO_DEVICE = ""
COMMAND_STATUS_FAILED = ""
COMMAND_STATUS_EXECUTING = ""
COMMAND_STATUS_SUCCESS = ""

class Command:
    def __init__(self):
        self.deviceID = ""
        self.ownerID = ""
        self.commandID =""
        self.code = ""
        self.status = ""
        self.plantId = ""
        self.lastUpdate = str(time.time()) 
        pass


def create_command(command):
    client.put_item(
        TableName=TABLE_NAME,
        Item={
            "commandID": {
                "S": command.commandID
            },
            "plantID":{
                "S": command.plantId
            },
            "deviceID": {
                "S": command.deviceID
            },
            "code": {
                "S": command.code
            },
            "status":{
                "S": COMMAND_STATUS_INIT
            },
            "lastUpdate":{
                "S": command.lastUpdate
            }
        }
    )
    return

def update_command_status(command):
    client.update_item(
        TableName=TABLE_NAME,
        Key= {
            "deviceID": command.deviceID,
            "plantID": command.plantID,
            "commandID": command.commandID
        },
        Item={
            "status": {
                "S": command.status
            },
            "lastUpdate": {
                "S": ""
            }
        }
    )
    return

def list_commands(deviceID):
    commands = client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression="deviceID=:deviceID",
        ExpressionAttributeValues={
            ":deviceID": {
                "S": deviceID
            }
        }
    )
    return commands
