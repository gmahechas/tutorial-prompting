import openai
import api_key

print(api_key.api_key)
# openai.api_key = api_key


# def get_completion(content, model="gpt-3.5-turbo"):
#     messages = [{"role": "user", "content": content}]
#     data = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=0,  # this is the degree of randomness of the model's output
#     )
#     print(data)
#     return data.choices[0].message["content"]
#
#
# text = f"""
# You should express what you want a model to do by \
# providing instructions that are as clear and \
# specific as you can possibly make them. \
# This will guide the model towards the desired output, \
# and reduce the chances of receiving irrelevant \
# or incorrect responses. Don't confuse writing a \
# clear prompt with writing a short prompt. \
# In many cases, longer prompts provide more clarity \
# and context for the model, which can lead to \
# more detailed and relevant outputs.
# """
# prompt = f"""
# Summarize the text delimited by triple backticks \
# into a single sentence.
# ```{text}```
# """
#
# print(prompt)
# response = get_completion(prompt)
# print(response)
