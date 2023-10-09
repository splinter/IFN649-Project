from table_clients.plants import create_plant,Plant

def from_event(event):
    data = event.data
    plant = {}
    plant["plantID"]=data.plantID
    plant["deviceID"]=data.deviceID
    return plant

def lambda_handler(event,context):
    plant = Plant(plantID="1", deviceID="2")
    create_plant(plant)
    res = {
        "status": 200
    }
    return res