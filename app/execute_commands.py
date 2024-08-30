
import subprocess

def execute_command(command: str):
    result = subprocess.run(command,capture_output=True,shell=True)
    print("! COMMAND RUNNED !")
    print("Standard Output:", result.stdout)
    print("Standard Error:", result.stderr)
    print("Return Code:", result.returncode)



    