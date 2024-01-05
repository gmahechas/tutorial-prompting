from open_ai import MyOpenAI

# prompt = f"""
# Translate the following English text to Spanish: \
# ```Hi, I would like to order a blender```
# """

prompt = f"""
Tell me which language this is: 
```Combien coûte le lampadaire?```
"""

print(prompt)
openai = MyOpenAI()
openai.completion(prompt)
