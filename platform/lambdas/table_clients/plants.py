import boto3

client = boto3.client('dynamodb')
TABLE_NAME = "IOT-Plants"


class Plant:
    def __init__(self):
        self.plantID = ""
        self.plantType = ""
        self.deviceID = ""
        pass

class PlantSensorData:
    def __init__(self) -> None:
        self.plantID = ""
        self.deviceID = ""
        self.temperature = ""
        self.humidity = ""
        pass
    def create(self,plantSensorData):
        result = client.update_item(
            TableName,
            AttributeUpdates={
                
            }
        )

class PlantAction:
    def __init__(self):
        pass

class PlantRepository:
    def __init__(self):
        pass

    def create(self,plant):
        result = client.update_item(
            TableName=TABLE_NAME,
            AttributeUpdates={
                "plantID": plant.plantID,
                "deviceID": plant.deviceID
            }
        )
        return result

class PlantSensorDataRepository:
    def __init__(self):

        pass

class PlantActionRepository:
    def __init__(self):
        pass

