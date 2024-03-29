import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../")))

from open_ai import MyOpenAI

# triple quotes: """
# triple backticks: ```
# triple dashes: ---
# angle brackets: <>
# XML tags: <tag>


text = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs.
"""
prompt = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text}```
"""

print(prompt)
openai = MyOpenAI()
# for response in openai.completion(prompt):
#     print(response, end="")
openai.completion(prompt)
