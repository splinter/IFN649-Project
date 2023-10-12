import requests
import configparser
import logging

configs = configparser.ConfigParser()
configs.read("clients.ini")

logger = logging.getLogger(__name__)

def fetch_commands():
    endpoint = configs["default"]["endpoint"]
    print("Making request to " + endpoint)
    results = requests.get(endpoint + "/devices/commands?deviceID=1")

    if(results.status_code !=200):
        return []
    response = results.json()
    if "data" in response:
        return response["data"]
    return []

def update_command(deviceID,commandID, status):
    endpoint = ""
    return True
    results = requests.put(endpoint,data={
        "deviceID": deviceID,
        "commandID": commandID,
        "status": status
    })
    return

def create_command(deviceID,plantID,operation):
    
    return