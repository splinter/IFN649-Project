import logging
import datetime
import network.commands as networkCommands
import time
class Scheduler:
    def __init__(self) -> None:
        self.cmdMap = {}
        self.cmdOpMap={}
        self.cmdOccurenceMap = {}
        pass
    def register_command(self,commands):
        print(commands)
        for command in commands:
            commandID = command["commandID"]
            if command["commandID"] in self.cmdMap:
                logging.info("Command skipped")
                pass
            commandOp = CommandOp(command)
            commandOp.parse()
            print(commandOp)
            self.cmdOpMap[commandID]= commandOp
            self.cmdMap[commandID] = command
    
    def schedule(self):
        print("Started scheduling")
        while True:
            for cmdId in self.cmdOpMap:
                print("Checking each command")

                if cmdId in self.cmdOccurenceMap:
                    lastOccurence = self.cmdOccurenceMap[cmdId]
            
                if cmdId not in self.cmdOccurenceMap:
                    lastOccurence = datetime.datetime.now()
                    self.cmdOccurenceMap[cmdId]=datetime.datetime.now()

                print(self.cmdMap[cmdId])
                occurenceSeconds = self.cmdOpMap[cmdId].occurenceSeconds
                print(occurenceSeconds)
    
                diff = datetime.datetime.now() - lastOccurence

                diffInSeconds = diff.total_seconds()
                print("Diff " + str(diffInSeconds) )

                if diffInSeconds > occurenceSeconds:
                    self.cmdOpMap[cmdId]
                    networkCommands.get_input_commands_queue().put(self.cmdOpMap[cmdId].code)
                    self.cmdOccurenceMap[cmdId]=datetime.datetime.now()
                    print("Putting command in queue")
            time.sleep(5)       

rateMap = {
    "SECOND": 1,
    "MIN": 60,
    "HOUR": 60 * 24
}

class CommandOp:
    def __init__(self,command) -> None:
        self.code = command["code"]
        self.invalidCommandOp=False
        self.occurence = None
        self.rate = None
        self.occurenceSeconds = None
        pass

    def parse(self):
        codeSplitBySpace = self.code.split("EVERY")
        print(codeSplitBySpace)
        if len(codeSplitBySpace) !=2:
            self.invalidCommandOp=True
            return
        commandCode = codeSplitBySpace[0]
        time = codeSplitBySpace[1]
        timeSplitBySpace = time.strip().split(" ")
        
        if len(timeSplitBySpace) != 2:
            print("Invalid command")
            self.invalidCommandOp = True
            return
        self.occurence = timeSplitBySpace[0]
        self.rate = timeSplitBySpace[1]
        print("Calculated rate " + self.rate)
        if self.invalidCommandOp:
            return
        self.parseRate()
        print("OccurentSeconds" + str(self.occurenceSeconds))
        return
    def parseRate(self):
        if self.rate in rateMap:
            self.occurenceSeconds = rateMap[self.rate] * int(self.occurence)
        return None
        