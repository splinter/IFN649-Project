from table_clients.plants import PlantRepository

def from_event(event):
    data = event.data
    plant = {}
    plant["plantID"]=data.plantID
    plant["deviceID"]=data.deviceID
    return plant

def lambda_handler(event,context):
    PlantRepository.create()
    res = {
        "status": 200
    }
    return res