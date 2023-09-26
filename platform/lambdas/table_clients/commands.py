import boto3

client = boto3.client("dynamodb")
TABLE_NAME = ""
KEY = ""

COMMAND_STATUS_INIT = ""
COMMAND_STATUS_SENT_TO_DEVICE = ""
COMMAND_STATUS_FAILED = ""
COMMAND_STATUS_EXECUTING = ""
COMMAND_STATUS_SUCCESS = ""

def create_document(command):
    doc = {}
    status = 
    doc["deviceID"] = command.deviceID
    doc["code"]=command.code
    doc["status"]=command.status
    return doc

class CommandRepository:
    def __init__(self):
        pass

    def create(coammnds):
        result = client.update_item(
            TableName=TABLE_NAME,
            Key={
                [KEY]: command.id
            },
            AttributeUpdates=create_document(commands)
        )
        return result
    def update_status(commandID,status):
        result = client.update_item(
            TableName=TABLE_NAME,
            Key={
                [KEY]: commandID
            },
            AttributeUpdates=create_document({
                
            })
        )
        return result
    def delete(self,commandID):
        return
    def list_users_commands(self,userId):
        return

class Command:
    def __init__(self):
        self.deviceID = ""
        self.id = ""
        self.code = ""
        self.status = ""
        self.plantId = ""
        pass
