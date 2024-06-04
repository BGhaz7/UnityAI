from openai import OpenAI

class OpenAIClient:
    def __init__(self, api_key, model='gpt3'):
        self.api_key = api_key
        self.model = model
        self.client = OpenAI(api_key = api_key)
    
    def generate_text(self, prompt, preprompt=None):
        messages = []
        if preprompt:
            messages.append({"role": "system", "content": preprompt})
        messages.append({"role": "user", "content": prompt})
        
        completion = self.client.chat.completions.create(
            model=self.model,
            messages=messages
        )
        return  completion.choices[0].message.content

