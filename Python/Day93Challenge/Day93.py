import sys
sys.path.append("C:/Users/user/Documents/Replit 100 Days Of Code/Python")
import env_vars
from requests.auth import HTTPBasicAuth
from flask import Flask, request
import requests
import os
import json


app = Flask(__name__)
static_url_path = '/static'


client_id = os.environ["CLIENT_ID"]
client_secret = os.environ["CLIENT_SECRET"]

url = "https://accounts.spotify.com/api/token"
data = {"grant_type": "client_credentials"}
auth = HTTPBasicAuth(client_id, client_secret)

response = requests.post(url, data=data, auth=auth)
access_token = response.json()["access_token"]
count = 0

def get_audio(year):
    global count
    if count == 10:
        count = 0

    display = 0
    url_list = []
    url = "https://api.spotify.com/v1/search"
    headers = {"Authorization": f"Bearer {access_token}"}
    search = f"?q=year%3A{year}&type=track&limit=10"

    full_url = f"{url}{search}"
    response = requests.get(full_url, headers=headers)
    data = response.json()
    for track in data['tracks']['items']:
        if display == count:
            url_list.append(track['artists'][0]['name'])
            url_list.append(track['name'])
            url_list.append(track['preview_url'])
        display += 1
    count += 1
    return url_list


@app.route('/')
def index():
    page = ""
    f = open(
        "C:/Users/user/Documents/Replit 100 Days Of Code/Python/Day93Challenge/Day93.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{audio}", "")
    return page


@app.route("/search", methods=["POST"])
def search():
    form = request.form
    year = form["year"]
    response = ""
    for i in range(0, 10):
        answers = get_audio(year)
        artists = answers[0]
        song_title = answers[1]
        song_source = answers[2]
        response += f"""
<h2>{song_title}</h2>
<h3>{artists}</h3>
<audio controls>
      <source src="{song_source}" type="audio/mpeg" />
      Your browser does not support the audio tag.
</audio>
"""
        response += "\n"

    page = ""
    f = open(
        "C:/Users/user/Documents/Replit 100 Days Of Code/Python/Day93Challenge/Day93.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{audio}", response)

    return page


app.run(host='0.0.0.0', port=5500)
