from open_ai import MyOpenAI

# Boie is a real company, the product name is not real.

prompt = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
print(prompt)
openai = MyOpenAI()
openai.completion(prompt)
