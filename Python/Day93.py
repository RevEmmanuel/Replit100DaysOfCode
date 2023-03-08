import requests
import os, time
import json
import env_vars
from requests.auth import HTTPBasicAuth

client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)
access_token = response.json()["access_token"]

artist = input("Enter an artist > ").lower()
artist = artist.replace(" ", "%20")
url = "https://api.spotify.com/v1/search"
headers = {"Authorization": f"Bearer {access_token}"}
search = f"?q=artist%3A{artist}&type=track&limit=10"

full_url = f"{url}{search}"
response = requests.get(full_url, headers=headers)
data = response.json()


for track in data['tracks']['items']:
    print(track['artists'][0]['name'])
    print(track['name'])
    print(track['preview_url'])
    time.sleep(2)

