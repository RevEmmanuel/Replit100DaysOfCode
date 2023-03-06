import requests
import json
import os

for i in range(0, 10):
    result = requests.get("https://randomuser.me/api/")
    if result.status_code != 200:
        print("Error, couldn't get response")
    else:
        user = result.json()
        print(json.dumps(user), 2)
        name = f"""{user["results"][0]["name"]["first"]} {user["results"][0]["name"]["last"]}"""
        print("This user is", name)

        image = f"""{user["results"][0]["picture"]["medium"]}"""
        image = requests.get(image)
        os.chdir(
            "C:/Users/user/Documents/Replit 100 Days Of Code/Python/Day90Creations")
        picture = open(f"{name}.jpg", "wb")
        picture.write(image.content)
        picture.close()
