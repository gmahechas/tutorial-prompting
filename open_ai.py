from openai import OpenAI


class MyOpenAI:
    model = "gpt-4"
    client: OpenAI

    def __init__(self):
        self.client = OpenAI(api_key="")

    def completion(self, content):
        for chunk in self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": content}],
            stream=True,
        ):
            print(chunk.choices[0].delta.content or "", end="")
            # yield chunk.choices[0].delta.content or ""  # example is in 01-delimiters.py
