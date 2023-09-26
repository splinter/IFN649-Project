import logging

def get_user(token):
    return

def is_user_owner(user,device):
    return True

def get_devices(context):
    return

def register_devices(user,devices):
    return

def register_device(user,device):
    if not is_user_owner(user,device):
        return False
    
    return

def handle(event,context):

    user = get_user(context.headers.token)
    devices = get_devices(context)

    results = register_devices(user,devices)
    
    return
