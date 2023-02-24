import os
import random
import time

user_list = []
try:
    with open("users", "x") as file:
        file = open("users", "r")
        data = file.read()
        user_list = eval(data)
        file.close()
except FileExistsError:
    with open("users", "r") as file:
        data = file.read()
        user_list = eval(data)
        file.close()


def check_if_username_exists(username):
    for users in user_list:
        used_names = users["username"]
        if username == used_names:
            return True
    return False


def find_user(username):
    for users in user_list:
        used_names = users["username"]
        if username == used_names:
            return users


def create_user():
    user_name = input("Enter your preferred username: ")
    while check_if_username_exists(user_name):
        print("Username already exists")
        user_name = input("Enter your preferred username: ")
    user_password = input("Enter your preferred password: ")
    salt = random.randint(1, 9000)
    user_password = f"{user_password}{salt}"
    user_password = hash(user_password)
    new_user = {"username": user_name, "salt": salt, "password": user_password}
    user_list.append(new_user)
    print("User created successfully")
    main_menu()


def login():
    user_name = input("Enter your username: ")
    if check_if_username_exists(user_name):
        found_user = find_user(user_name)
        salt = found_user["salt"]
        user_password = input("Enter your password: ")
        user_password = f"{user_password}{salt}"
        user_password = hash(user_password)
        if user_password == found_user["password"]:
            print(f'Login successful! \nHi {found_user["username"]}')
            time.sleep(3)
            main_menu()
        else:
            print("Login failed")
            time.sleep(2)
            exit()

    else:
        print("User not found! ")
        main_menu()


def main_menu():
    time.sleep(1)
    os.system("cls")
    while True:
        choice = input("1. Create User \n2. Login \nElse: Exit \n")
        if choice == '1':
            time.sleep(1)
            os.system("cls")
            create_user()
        elif choice == '2':
            time.sleep(1)
            os.system("cls")
            login()
        else:
            time.sleep(1)
            os.system("cls")
            print("Bye! ")
            time.sleep(1)
            f = open("users", "w")
            f.write(str(user_list))
            f.close()
            exit()
    f = open("users", "w")
    f.write(str(user_list))
    f.close()


main_menu()