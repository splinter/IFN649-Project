import boto3

client = boto3.client('dynamodb')
TABLE_NAME = "IOT-Plants"


class Plant:
    def __init__(self, plantID, deviceID, ownerID):
        self.plantID = plantID
        self.deviceID = deviceID
        self.ownerID = ownerID
        self.plantStatus = ""
        pass

def create_plant(plant):
    client.put_item(
        TableName=TABLE_NAME,
        Item={
            "plantID":{
                "S": plant.plantID
            },
            "deviceID": {
                "S": plant.deviceID
            }
        }
    )
    return 

def list_plants(ownerID):
    result = client.query(
        TableName= TABLE_NAME,
        KeyConditionExpression=(
            Key("ownerID").eq(ownerID)
        )
    )
    return

