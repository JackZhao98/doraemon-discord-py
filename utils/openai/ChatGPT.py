import openai
import json
# import openai helper
from utils.openai.openai_helper import create_chat_completion

class OpenAIChat:
    def __init__(self, api_key, org):
        self.api_key = api_key
        self.org = org
        openai.api_key = api_key
        openai.organization = org
        self.messages={}

    def process_message(self, message, uid):
        if uid not in self.messages.keys():
            self.messages[uid] = []
        self.messages[uid].append(message)

    def clear_message(self, uid):
        if uid in self.messages.keys():
            self.messages[uid].clear()

    def clear_all(self):
        self.messages.clear()

    def chat(self, message, uid):
        request = {"role": "user", "content": message}
        self.process_message(request, uid)

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.messages[uid]
        )
        response_msg = response.choices[0].message
        self.process_message(response_msg, uid)
        return response_msg.content



    def generate_response(self, model_id, messages, temperature=1, top_p=1, n=1, stream=False, stop=None, max_tokens=1000, presence_penalty=0, frequency_penalty=0, logit_bias=None, user=None,):
        response = openai.Completion.create(
            model=model_id,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            n=n,
            stream=stream,
            stop=stop,
            max_tokens=max_tokens,
            frequency_penalty=frequency_penalty,
            presence_penalty=presence_penalty,
            logit_bias=logit_bias,
            user=user
        )
        response_str =  json.dumps(response, indent=4)
        return create_chat_completion(response_str)


