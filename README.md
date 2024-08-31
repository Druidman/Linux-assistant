# Linux-assistant

## What is it?
An (ai (bruh)) assistant used to launch applications search web etc. and help you use linux

## How does it work?
When you type command it is being processed by llama3 70b tool-use GROQ llm then command is being returned to the program and executed

# RUN
IN REPO DIRECTORY: `/Linux-assistant`

Make .env file in repo directory:
![Screenshot](/images/env_file.png)

Install dependencies: `pip3 install -r requirements.txt`

Run: `python3 run.py`

# `sys_prompt_vars.py` info: 
This file is stored in: `/app/prompts/sys_prompt_vars.py`.
Used to store NOT REQUIRED additional variables.
This variables will be added to the assistant system prompt.

My example configured variables:
![Screenshot](/images/myvars.png)

You can configure this vars as you like but if you add new one it won't be added to system prompt.

