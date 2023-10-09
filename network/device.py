import requests

okStatus = "OK"

def heartbeat_device():
    return True
    endpoint = ""
    requests.put(endpoint,data={
        "status": okStatus
    })
    return