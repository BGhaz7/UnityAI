import core as unity

client_gpt3 = unity.get_client('openai-gpt3', 'your-api-key')
result = client_gpt3.generate_text('Once upon a time', 'Mention a dragon in the story')
print(result)