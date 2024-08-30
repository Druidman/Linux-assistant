import os,json
from groq import Groq
from dotenv import load_dotenv


load_dotenv()

class Assistant():
    def __init__(self,model: str,sys_prompt: str):
       
        self.llm = model
        self.system_prompt = sys_prompt

        self.model_provider = Groq(api_key=os.environ.get("GROQ_API_KEY"))
        
    def generate_command(self,user_prompt: str) -> str:
        response = self.model_provider.chat.completions.create(
            model=self.llm,
            messages=[
                {
                    "role": "system",
                    "content": self.system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            temperature=0.5,
            max_tokens=1024,
            top_p=0.65,
            stream=False,
            response_format={"type": "json_object"},
            stop=None,
        )
        response = json.loads(response.choices[0].message.content)
        return response['command']

        

        


