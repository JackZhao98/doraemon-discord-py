import openai


completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-0301", 
  messages=[{"role": "user", "content": "Tell the world about the ChatGPT API in the style of a pirate."}]
)

print(completion)