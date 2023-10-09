import queue 

inputCommandQueue = queue.Queue()
outputCommandQueue = queue.Queue()

def add_commands(commands):
    for command in commands:
        inputCommandQueue.put(command)
    return

def update_commands(commands):
    for command in commands:
        outputCommandQueue.put(command)
    return

def get_input_commands_queue():
    return inputCommandQueue

def get_output_commands_queue():
    return outputCommandQueue

def build_command_from_str(commandStr):
    return 