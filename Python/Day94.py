import requests
import json
import os
import openai
import env_vars

openai.organization = os.environ['organisation_id']
openai.api_key = os.environ['openai']
openai.Model.list()

country = "ng"
news = os.environ['news_api']
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}"
result = requests.get(url)
data = result.json()

prompt = "Who is the most handsome bald man?"
response = openai.Completion.create(
    model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=6)
print(response["choices"][0]["text"].strip())

counter = 0
for article in data["articles"]:
    if counter == 5:
        break
    prompt = (f"""Summarise {article["url"]} in one sentence.""")
    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=50)
    print(response["choices"][0]["text"].strip())
    counter += 1
