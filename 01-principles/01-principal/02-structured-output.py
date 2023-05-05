from OpenAI import OpenAI

prompt = f"""
Generate a list of three made-up book titles along \ 
with their authors and genres. 
Provide them in JSON format with the following keys: 
book_id, title, author, genre.
"""

print(prompt)
openai = OpenAI()
response = openai.get_completion(prompt)
print(response)
