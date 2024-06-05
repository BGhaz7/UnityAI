import unityAI
import os
from dotenv import load_dotenv
load_dotenv()
# client_gpt3 = unityAI.get_client('openai-dalle3', os.getenv("OPENAI_API_KEY"))
# result = client_gpt3.generate_text("Hello, how are you?")
client_gemini = unityAI.get_client('gemini', os.getenv("GEMINI_API_KEY"))
result = client_gemini.generate_text("Hello, how are you? Are you google?")
print(result)