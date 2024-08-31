
import os

def execute_command(command: str):
    try:
        os.system(command)
    except:
        print("Command ended: ", command)
    



    