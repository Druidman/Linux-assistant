from app import run,construct_system_prompt

sys_prompt = construct_system_prompt()

run(sys_prompt=sys_prompt)