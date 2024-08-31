from .assistant import Assistant
from .execute_commands import execute_command
from threading import Thread

def next_command():
    result = str(input("\nNext command? (Y or N)")).upper()
    if result == 'Y':
        return True
    else:
        return False
    
def run(sys_prompt: str):
    
    threads = []
    while next_command():
        prompt = str(input("Ask assistant something: "))
        print("Generating command...\n")

        assistant = Assistant("llama-3.1-70b-versatile",sys_prompt=sys_prompt)
        command = assistant.generate_command(user_prompt=prompt)

        print(f"Command: {command}\n")

        check = str(input("\nExecute this command? (Y or N)\n")).upper()

        if check == 'Y':
            print("Executing command...\n\n")
            thread = Thread(target=execute_command, args=(command,))
            thread.start()
            threads.append(thread)
        else:
            print("Command aborted\n")

    for i in threads:
        i.join()