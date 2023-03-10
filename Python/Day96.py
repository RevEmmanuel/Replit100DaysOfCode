import requests
from bs4 import BeautifulSoup

# url = "https://www.tripadvisor.com/Restaurants-g304026-Lagos_Lagos_State.html"
# print(0)
# response = requests.get(url)
# print(1)
# html = response.text
# soup = BeautifulSoup(html, "html.parser")
# my_links = soup.find_all("a", {"class": "Lwqic Cj b"})
# print(len(my_links))

# for link in my_links:
#     print(link.text)
#     print(f"""https://www.tripadvisor.com{link["href"]}""")



url = "https://news.ycombinator.com/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")
myLinks = soup.find_all("span", {"class": "titleline"})

for link in myLinks:
    text = link.text
    if "python" in text.lower() or "replit" in text.lower():
        print("Headline:", text)
        my_link = link.find_all("a")
        print(my_link[0]["href"])
    