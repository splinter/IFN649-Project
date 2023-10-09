import requests
import configparser


def fetch_commands():
    return []
    endpoint = ""
    results = requests.get(endpoint)
    data = results.data
    return 

def update_command(deviceID,commandID, status):
    endpoint = ""
    return True
    results = requests.put(endpoint,data={
        "deviceID": deviceID,
        "commandID": commandID,
        "status": status
    })
    return