import boto3
import logging
from boto3 import Key

client = boto3.client("dynamodb")

TABLE_NAME = "IOT-Devices"


class Device:
    def __init__(self):
        self.ownerID = ""
        self.deviceID = ""
        self.plantID = ""
        self.deviceName = ""
        self.deviceToken = ""
        pass

def create_device(device: Device):
    result = client.create_item(
        TableName=TABLE_NAME,
        Item={
            "deviceID":{ 
                "S": device.deviceID
            },
            "ownerID": {
                "S": device.ownerID
            },
            "plantID": {
                "S": device.plantID
            },
            "deviceName": {
                "S": device.deviceName
            }
        }
    )
    print(result)
    return result

def list_devices(ownerID):
    result = client.query(
        TableName= TABLE_NAME,
        KeyConditionExpression=(
            Key("ownerID").eq(ownerID)
        )
    )
    return 

def update_device_status(deviceID,status):
    client.update_item(
        TableName=TABLE_NAME,
        Key={
            "deviceID": deviceID
        },
        Item={
            "status": status
        }
    )
    return
    