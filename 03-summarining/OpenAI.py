import openai


class OpenAI:

    model = "gpt-3.5-turbo"

    def __init__(self):
        openai.api_key = ''

    def get_completion(self, content):
        messages = [{"role": "user", "content": content}]
        data = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=0,  # this is the degree of randomness of the model's output
        )
        print(data)
        return data.choices[0].message["content"]
