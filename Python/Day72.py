import os
import time
import datetime
import random


diary_list = []
salt = random.randint(1, 10000)
try:
    with open("diary", "x") as file:
        file = open("diary", "r")
        data = file.read()
        diary_list = eval(data)
        file.close()
except FileExistsError:
    with open("diary", "r") as file:
        data = file.read()
        diary_list = eval(data)
        file.close()

password = ""
password = input("Set your password: > ")
password = f"{salt}--{password}"
password = hash(password)
print("Password saved!")
time.sleep(2)
os.system("cls")

def login(entered_password):
    entered_password = f"{salt}--{entered_password}"
    return hash(entered_password) == password


def add_entry():
    event = input("Enter the entry : > ").strip()
    time_created = datetime.datetime.now()
    diary_entry = {time_created: event}
    diary_list.append(diary_entry)
    print("Added! ")
    time.sleep(1)
    os.system("cls")


def view_entries():
    for event in diary_list[::-1]:
        print("Most recent entry >", event)
        if (input("View next entry? (y/n) > ") == "n"):
            time.sleep(1)
            os.system("cls")
            break
        time.sleep(1)
        os.system("cls")


def main_menu():
    os.system("cls")
    while True:
        choice = input("1. Add\n2. View\nElse: Exit > ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        else:
            break


answer = input("Enter your password: > ")
if login(answer):
    print("Password correct! Proceeding to main meu")
    time.sleep(2)
    main_menu()
    f = open("diary", "w")
    f.write(str(diary_list))
    f.close()
else:
    print("Incorrect password. \nExiting app")
    time.sleep(2)
    os.system("cls")
    exit(0)

print("Thanks for using diary!")
