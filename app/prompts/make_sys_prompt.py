from .sys_prompt_vars import *
import os

def construct_system_prompt():

    score = 50
   
    common_apps = COMMON_APPS
    if common_apps:
        score +=20
    else:
        common_apps = ''

    common_websites = COMMON_WEBSITES
    if common_websites:
        score += 10
    else:
        common_websites = ''

    system_data = SYSTEM_DATA
    if system_data:
        score += 15
    else:
        system_data = ''

    user_data = USER_DATA
    if user_data:
        score += 5
    else:
        user_data = ''    

    print(f"Your assistant will work on {score}% of its power on your pc")

    additionals = f"""

    Here is list of commonly used apps/websites and helpfull terms:

    Commonly used apps (installed):
    {common_apps}

    Commonly visited websites (on web-browser that user specified in common apps):
    {common_websites}

    System data (helpfull for command generation):
    {system_data}

    User_data (about your pilot):
    {user_data}
    """

    path = os.path.dirname(__file__)
    path = os.path.dirname(path)
    path = os.path.join(path,"constants")
    file_path = os.path.join(path,"sys_prompt.txt")

    with open(file_path, "r") as file:
        sys_prompt = file.read()
        
        file.close()

    prompt =  sys_prompt + additionals
    return prompt