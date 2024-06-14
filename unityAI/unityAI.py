from ai_clients.openai_client import OpenAIClient
from ai_clients.gemini_client import GeminiClient

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

class GeminiCore(unityAI):
    def __init__(self, api_key, model='gemini-1.5-flash'):
        super().__init__(api_key)
        self.client = GeminiClient(api_key, model)
    
    def generate_text(self, prompt, **kwargs):
        return self.client.generate_text(prompt)

def get_client(service, api_key):
    openai_service_model_mapping = {
        'openai': 'gpt-3.5-turbo',
        'openai-gpt3': 'gpt-3.5-turbo',
        'openai-gpt4': 'gpt-4',
        'openai-gpt4o': 'gpt-4o',
        'openai-dalle3': 'dall-e-3',
        'openai-dalle2': 'dall-e-2',
    }
    google_service_model_mapping = {
        'gemini': 'gemini-1.5-flash',
        'gemini-1.5-pro': 'gemini-1.5-pro-latest',
    }

    if service in openai_service_model_mapping:
        return OpenAICore(api_key, openai_service_model_mapping[service])
    elif service in google_service_model_mapping:
        return GeminiCore(api_key, google_service_model_mapping[service])
    else:
        raise ValueError(f"Service {service} is not supported.")