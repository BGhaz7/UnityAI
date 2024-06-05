from ai_clients.openai_client import OpenAIClient

class unityAI:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_text(self, prompt: str, **kwargs):
        raise NotImplementedError("This method should be overridden by subclasses")

class OpenAICore(unityAI):
    def __init__(self, api_key, model='gpt3.5'):
        super().__init__(api_key)
        self.client = OpenAIClient(api_key, model)

    def generate_text(self, prompt, pre_prompt=None, **kwargs):
        return self.client.generate_text(prompt, pre_prompt)
    
    def generate_image(self, prompt, asImage = False, imageName = None, size = '1024x1024', quality = "standard", n = 1, **kwargs):
        return self.client.generate_image(prompt, asImage, imageName, size, quality, n, **kwargs)

def get_client(service, api_key):
    if service == 'openai' or service == 'openai-gpt3':
        return OpenAICore(api_key, 'gpt-3.5-turbo')
    elif service == 'openai-gpt4':
        return OpenAICore(api_key, 'gpt-4')
    elif service == 'openai-gpt4o':
        return OpenAICore(api_key, 'gpt-4o')
    elif service == 'openai-dalle3':
        return OpenAICore(api_key, 'dall-e-3')
    elif service == 'openai-dalle2':
        return OpenAICore(api_key, 'dall-e-2')
    else:
        raise ValueError(f"Service {service} is not supported.")
