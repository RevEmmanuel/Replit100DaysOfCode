import requests, random, os, time
import json

jokes_list = []
try:
    with open("jokes", "x") as file:
        file = open("jokes", "r")
        data = file.read()
        jokes_list = eval(data)
        file.close()
except FileExistsError:
    with open("jokes", "r") as file:
        data = file.read()
        jokes_list = eval(data)
        file.close()


def show_new_joke():
    result = requests.get("https://icanhazdadjoke.com/",
                          headers={"Accept": "application/json"})
    joke = result.json()
    joke = joke["joke"]
    print(joke)
    return joke



while True:
    the_joke = show_new_joke()
    choice = input(
        "Enter 's' to save joke, 'l' to load old jokes, 'n' to see a new joke or 'r' to exit. >").lower().strip()
    if choice == "s":
        jokes_list.append(the_joke)
        print("Added joke")
        time.sleep(1)
        os.system("cls")
        choice = input(
            "Enter 'n' to see a new joke or 'r' to exit. >   ").lower().strip()
        if choice == "n":
            continue
        else:
            break
    elif choice == "l":
        random_joke = random.choice(jokes_list)
        time.sleep(1)
        os.system("cls")
        print(random_joke)
        choice = input(
            "Enter 'n' to see a new joke or 'r' to exit. >").lower().strip()
        if choice == "n":
            continue
        else:
            break
    elif choice == "n":
        continue
    elif choice == "r":
        break

print("Done!")
f = open("jokes", "w")
f.write(str(jokes_list))
f.close()
