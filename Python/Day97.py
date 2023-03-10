import requests
import os
import openai
import env_vars
from bs4 import BeautifulSoup

openai.organization = os.environ['organisation_id']
openai.api_key = os.environ['openai']
openai.Model.list()

url = "https://en.wikipedia.org/wiki/Hair_loss"
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, "html.parser")
my_links = soup.find_all("ol", {"class": "references"})


prompt = (f"""Summarise {url} in three paragraphs.""")
response = openai.Completion.create(
    model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=50)
print(response["choices"][0]["text"].strip())
print("References: ")
print(my_links[0].text.replace("^", "-").strip())
