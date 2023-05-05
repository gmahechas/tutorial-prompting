# give successful examples of completing task
# then ask model to perform the task

from OpenAI import OpenAI

prompt = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience.

<grandparent>: The river that carves the deepest \ 
valley flows from a modest spring; the \ 
grandest symphony originates from a single note; \ 
the most intricate tapestry begins with a solitary thread.

<child>: Teach me about resilience.
"""
print(prompt)
openai = OpenAI()
response = openai.get_completion(prompt)
print(response)
