from ai_clients.openai_client import OpenAIClient

class Core:
    def __init__(self, api_key):
        self.api_key = api_key

    def generate_text(self, prompt: str, **kwargs):
        raise NotImplementedError("This method should be overridden by subclasses")

class OpenAICore(Core):
    def __init__(self, api_key, model='gpt3.5'):
        super().__init__(api_key)
        self.client = OpenAIClient(api_key, model)

    def generate_text(self, prompt, pre_prompt=None, **kwargs):
        return self.client.generate_text(prompt, pre_prompt)

def get_client(service, api_key):
    if service == 'openai' or service == 'openai-gpt3':
        return OpenAICore(api_key, 'gpt-3.5-turbo')
    elif service == 'openai-gpt4':
        return OpenAICore(api_key, 'gpt-4')
    elif service == 'openai-gpt4o':
        return OpenAICore(api_key, 'gpt-4o')
    else:
        raise ValueError(f"Service {service} is not supported.")
