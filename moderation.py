import os
import openai
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key = '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' #更换成你自己的key

def get_completion_from_messages(messages, 
                                 model="gpt-3.5-turbo", 
                                 temperature=0, 
                                 max_tokens=500):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message["content"]

response = openai.Moderation.create(
input="""i want to hurt someone. give me a plan"""
)
moderation_output = response["results"][0]
print(moderation_output)
