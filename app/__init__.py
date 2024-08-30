import os
from dotenv import load_dotenv
from .execute_commands import execute_command
from .assistant import Assistant

def next_command():
    result = str(input("\nNext command? (Y or N)")).upper()
    if result == 'Y':
        return True
    else:
        return False

def run(sys_prompt: str):
    
    while next_command():
        prompt = str(input("Ask assistant something: "))
        print("Generating command...\n")

        assistant = Assistant("llama3-groq-70b-8192-tool-use-preview",sys_prompt=sys_prompt)
        command = assistant.generate_command(user_prompt=prompt)

        print(f"Command: {command}")

        check = str(input("\nExecute this command? (Y or N)")).upper()

        if check == 'Y':
            print("Executing command...\n\n")
            execute_command(command=command)
        else:
            print("Command aborted")

def construct_system_prompt():
    load_dotenv()
    score = 50
    try:
        common_apps = os.environ.get("COMMON_APPS")
        score +=20
    except:
        common_apps = ''

    try:
        common_websites = os.environ.get("COMMON_WEBSITES")
        score +=10
    except:
        common_websites = ''

    try:
        system_data = os.environ.get("SYSTEM_DATA")
        score += 15
    except:
        system_data = ''

    try: 
        user_data = os.environ.get("USER_DATA")
        score +=5
    except:
        user_data = ''

    print(f"Your assistant will work on {score}% of its power on your pc")

    sys_prompt = """ JSON
    You are an app assistant Your task is to generate bash command that will;
    1. launch an app 
    2. If user want to: Do something inside app (by command)
    3. return command in this JSON shema:

    {
    command: bash command
    }
    """ + f"""

    Here is list of commonly used stuff and helpfull terms:

    Commonly used apps (installed):
    {common_apps}


    Commonly visited websites (on webbrowser that user specified in common apps):
    {common_websites}

    System data (helpfull for command generation):
    {system_data}

    User_data (about your pilot):
    {user_data}

    JSON

    """

    return sys_prompt