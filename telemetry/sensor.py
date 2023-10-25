import datetime
from network.edge import recievedDataQueue
from clients.plants import update_plant_data

frequncy_update=10
class SensorTelemetry:
    def register(self, data):
        return

    def parse_data(self,data):
        dataBySpace = data.split(" ")
        item = {}
        for i in dataBySpace:
            kv = i.split("=")
            if len(kv) < 2:
                pass
            if kv[0] == "HUMIDITY":
                item["humidity"]=kv[1]
        return item
    
    def read_send(self):
        lastUpdate = datetime.time()
        while True:
            item = recievedDataQueue.get()
            plantData = self.parse_data(item)
            now = datetime.datetime()
            diff = lastUpdate - now
            if diff > frequncy_update:
                update_plant_data("1","1",plantData["humidity"])
        return

    

