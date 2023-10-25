import boto3
import time

client = boto3.client('dynamodb')
TABLE_NAME = "IOT-Plants"


class PlantData:
    def __init__(self, plantID, deviceID):
        self.plantID = plantID
        self.deviceID = deviceID
        self.soilTemperature = ""
        self.humidity = ""
        self.time = str(time.time())
        pass



def create_plant_data(plantData):
    client.put_item(
        TableName=TABLE_NAME,
        Item={
            "plantID":{
                "S": plantData.plantID
            },
            "deviceID": {
                "S": plantData.deviceID
            },
            "soilTemperature": {
                "S": str(plantData.soilTemperature)
            },
            "humidity": {
                "S": str(plantData.humidity)
            },
            "time": {
                "S": plantData.time
            }
        }
    )
    return 

keys = ["plantID","deviceID","commandID","code","status","lastUpdate"]
sKey ="S"
def converter(map):
    item = {}
    for key in keys:
        if key in map:
            item[key]=map[key][sKey]
    return item 
def get_plant_data(deviceID):
    results=client.query(
        TableName=TABLE_NAME,
        KeyConditionExpression="deviceID=:deviceID",
        ExpressionAttributeValues={
            ":deviceID":{
                "S": deviceID
            }
        }       
    )
    return

