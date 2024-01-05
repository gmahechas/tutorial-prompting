from openai import OpenAI, AsyncOpenAI


class MyOpenAI:
    model = "gpt-4"
    client: OpenAI
    async_client: AsyncOpenAI
    api_key = ""

    def __init__(self):
        self.client = OpenAI(api_key=self.api_key)
        self.async_client = AsyncOpenAI(api_key=self.api_key)

    def completion(self, content, temperature=0):
        for chunk in self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": content}],
                stream=True,
                temperature=temperature,  # this is the degree of randomness of the model's output
        ):
            print(chunk.choices[0].delta.content or "", end="")
            # yield chunk.choices[0].delta.content or ""  # example is in 01-delimiters.py

    async def completion_async(self, content):
        return await self.async_client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": content}],
            stream=True,
            temperature=0,
        )
