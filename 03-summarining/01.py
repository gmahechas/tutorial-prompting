from open_ai import MyOpenAI

prod_review = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \
super cute, and its face has a friendly look. It's \
a bit small for what I paid though. I think there \
might be other options that are bigger for the \
same price. It arrived a day earlier than expected, \
so I got to play with it myself before I gave it \
to her.
"""

# Summarize with a word/sentence/character limit
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site.
#
# Summarize the review below, delimited by triple
# backticks, in at most 30 words.
#
# Review: ```{prod_review}```
# """

# Summarize with a focus on shipping and delivery
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# Shipping department.
#
# Summarize the review below, delimited by triple
# backticks, in at most 30 words, and focusing on any aspects \
# that mention shipping and delivery of the product.
#
# Review: ```{prod_review}```
# """

# Summarize with a focus on price and value
# prompt = f"""
# Your task is to generate a short summary of a product \
# review from an ecommerce site to give feedback to the \
# pricing department, responsible for determining the \
# price of the product.
#
# Summarize the review below, delimited by triple
# backticks, in at most 30 words, and focusing on any aspects \
# that are relevant to the price and perceived value.
#
# Review: ```{prod_review}```
# """

# Try "extract" instead of "summarize"
prompt = f"""
Your task is to extract relevant information from \
a product review from an ecommerce site to give \
feedback to the Shipping department.

From the review below, delimited by triple quotes \
extract the information relevant to shipping and \
delivery. Limit to 30 words.

Review: ```{prod_review}```
"""

print(prompt)
openai = MyOpenAI()
openai.completion(prompt)
