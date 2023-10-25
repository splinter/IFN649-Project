import json
from table_clients.plants import PlantData, create_plant_data

def get_data(event):
    bodyStr = event["body"]
    body = json.loads(bodyStr)
    plantData = PlantData("1","1")
    plantData.plantID = body["plantID"]
    plantData.deviceID = body["deviceID"]
    plantData.humidity = body["humidity"]
    return plantData

def lambda_handler(event,contex):
    plantData = get_data(event)
    success = create_plant_data(plantData)
    return {
        "status":"success"
    }