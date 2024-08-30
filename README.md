# Linux-assistant

## What is it?
An (ai (bruh)) assistant used to launch applications search web etc. and help you use linux

## How does it work?
When you type command it is being processed by llama3 70b tool-use GROQ llm then command is being returned to the program and executed

# RUN
IN REPO DIRECTORY: `/Linux-assistant`

Make .env file in repo directory:
![Screenshot](/images/env-file.png)

Install dependencies: `pip3 install -r requirements.txt`

Run: `python3 run.py`

# .ENV info:
// If you want multiline use: \ on end of line. // 



## COMMON_APPS 

HELPS A TON 

### FORMAT
`<Number>. name (what is it) launch name: (what command is used to launch this app), \`

Example:
1. vivaldi (web browser) launch name: vivaldi, \

## COMMON_WEBSITES 

Does a lot if you use web browser often

### FORMAT
`<Number>. website name, \`

Example:
1. YouTube, \

## SYSTEM_DATA 

Does something about 10% increase in performance

### FORMAT

`<Number>. (what): (what is it), \`
Example:
1. distro: arch, \

## USER_DATA 

Does almost nothing about 5% increase in performance

### FORMAT

`<Number>. (smth about u)`

Example:
1. Hates ai, \

