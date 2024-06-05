import google.generativeai as genai
class GeminiClient:
    def __init__(self, api_key, model='gemini-1.5-flash'):
        self.api_key = api_key
        genai.configure(api_key = api_key)
        self.model = model
        self.client = genai.GenerativeModel(model)
    
    def generate_text(self, prompt):
        response = self.client.generate_content(prompt)
        return response.text