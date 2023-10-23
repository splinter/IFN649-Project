import boto3
import time

client = boto3.client('dynamodb')
TABLE_NAME = "IOT-Plants"


class PlantData:
    def __init__(self, plantID, deviceID, ownerID):
        self.plantID = plantID
        self.deviceID = deviceID
        self.ownerID = ownerID
        self.soilTemperature = ""
        self.humidity = ""
        self.time = str(time.now())
        pass



def create_plant_data(plantData):
    client.create_item(
        TableName=TABLE_NAME,
        Item={
            "plantID":{
                "S": plantData.plantID
            },
            "deviceID": {
                "S": plantData.deviceID
            },
            "ownerID":{
                "S": plantData.ownerID
            },
            "soilTemperature": {
                "N": str(plantData.soilTemperature)
            },
            "humidity": {
                "N": str(plantData.humidity)
            },
            "time": {
                "S": plantData.time
            }
        }
    )
    return 


