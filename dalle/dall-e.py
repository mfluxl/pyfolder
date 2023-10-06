import os
import openai

openai.api_key = "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"

userprompt = input("Write your divine text to generate a holy image: ")

response = openai.Image.create(
    prompt=userprompt,
    n=1,
    size="1024x1024"
)

image_url = response['data'][0]['url']
print(image_url)

