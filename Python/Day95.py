import requests
import os
import openai
import json
import env_vars
from requests.auth import HTTPBasicAuth

search_list = []

# newsapi
country = "ng"
news = os.environ['news_api']
url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={news}"
result = requests.get(url)
data = result.json()


# openai
openai.organization = os.environ['organisation_id']
openai.api_key = os.environ['openai']
openai.Model.list()

counter = 0
for article in data["articles"]:
    if counter == 5:
        break
    prompt = (f"""Summarise {data["articles"]["url"]} in three words.""")
    response = openai.Completion.create(
        model="text-davinci-002", prompt=prompt, temperature=0, max_tokens=50)
    response = response["choices"][0]["text"].strip()
    search = response.replace(" ", "%20")
    search = search.replace(".", "")
    search_list.append(search)
    counter += 1



# spotifyapi
client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]
url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)
access_token = response.json()["access_token"]

for search in search_list:
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    search = f"?q={search}&type=track&limit=1"

    full_url = f"{url}{search}"
    response = requests.get(full_url, headers=headers)
    data = response.json()
    print("News is", search)
    try:
        print("Artist", data['tracks']['items']['artists'][0]['name'])
        print("Song title", data['tracks']['items']['name'])
        print("Listen now at:", data['tracks']['items']['preview_url'])
    except:
        print("Nothing found for news!")
