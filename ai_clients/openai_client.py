from openai import OpenAI
import requests
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
    
    def generate_image(self, prompt, asImage = False, imageName = None, size = '1024x1024', quality = "standard", n = 1, **kwargs):
        completion = self.client.images.generate(
            model=self.model,
            prompt=prompt,
            size=size,
            quality=quality,
            n=n
        )
        if asImage:
            img_data = requests.get(completion.data[0].url).content
            with open(imageName+'.jpg', 'wb') as handler:
                handler.write(img_data)
                return imageName+'.jpg created successfully.'
            
        else:
            return completion.data[0].url
