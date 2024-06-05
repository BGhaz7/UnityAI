import unityAI

client_gpt3 = unityAI.get_client('openai-dalle3', 'api_key')
result = client_gpt3.generate_image('Sir', True, 'Sir')
print(result)