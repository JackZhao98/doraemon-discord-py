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

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

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

        try:
            chatResponse = self.generate_response(
                model_id="gpt-3.5-turbo-0301",
                messages=self.messages[uid],
                temperature=0.9,
                max_tokens=2000,
                frequency_penalty=0.5,
                presence_penalty=0.6,
            )
        except openai.error.InvalidRequestError as e:
            print(e)
            return "请使用 `-clear` 清除历史消息并重试。 Please try to use `-clear` to clear your chat history and try again."

        if len(chatResponse.choices) == 0:
            return "请使用 `-clear` 清除历史消息并重试。 Please try to use `-clear` to clear your chat history and try again."
        
        response_msg = chatResponse.choices[0].message
        self.process_message(response_msg.toDict(), uid)
        return response_msg.content



    def generate_response(self, model_id, messages, temperature=1, top_p=1, n=1, stream=False, stop=None, max_tokens=1000, presence_penalty=0, frequency_penalty=0,):
        response = openai.ChatCompletion.create(
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
        )
        response_str = json.dumps(response, indent=4)
        return create_chat_completion(response_str)