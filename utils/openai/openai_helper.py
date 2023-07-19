# import json
# from typing import List

# class ChatMessage:
#     def __init__(self, role: str, content: str):
#         self.role = role
#         self.content = content

#     def toDict(self):
#         return {
#             'role': self.role,
#             'content': self.content
#         }
    
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# class ChatCompletionChoice:
#     def __init__(self, index: int, message: ChatMessage, finish_reason: str):
#         self.index = index
#         self.message = message
#         self.finish_reason = finish_reason

#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# class ChatCompletion:
#     def __init__(self, id: str, created: int, choices: List[ChatCompletionChoice], usage: dict):
#         self.id = id
#         self.created = created
#         self.choices = choices
#         self.usage = usage
    
#     def toJSON(self):
#         return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

# def create_chat_completion(json_str: str) -> ChatCompletion:
#     json_obj = json.loads(json_str)
#     id = json_obj['id']
#     created = json_obj['created']
#     choices = []
#     for choice in json_obj['choices']:
#         index = choice['index']
#         message = ChatMessage(choice['message']['role'], choice['message']['content'])
#         finish_reason = choice['finish_reason']
#         choices.append(ChatCompletionChoice(index, message, finish_reason))
#     usage = json_obj['usage']
#     return ChatCompletion(id, created, choices, usage)