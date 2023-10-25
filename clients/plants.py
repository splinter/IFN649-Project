import logging
import requests
import configparser

configs = configparser.ConfigParser()
configs.read("clients.ini")

def update_plant_data(deviceID,plantID, humidity):
    endpoint = configs["default"]["endpoint"] + "/plants/sensor?deviceID=1"
    results = requests.put(endpoint,data= {
        "deviceID": deviceID,
        "plantID": plantID,
        "humidity": humidity
    })
    return
