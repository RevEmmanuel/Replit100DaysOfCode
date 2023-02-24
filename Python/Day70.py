import os, env_vars

admin_password = os.environ['ADMIN_PASSWORD']
normy_password = os.environ['PASSWORD']

type = input("Select Type: \n1. Admin\n2. Normal User > ")
password = ""
if type == '1':
    password = input('Hi Admin, Please enter your password: > ')
    if password == admin_password:
        print("Welcome, Admin! ")
    else:
        print("Intruder.!!!")
elif type == '2':
    user_name = input('Enter your username: > ')
    password = input('Enter your password: > ')
    if password == normy_password:
        print("Welcome,", user_name, "! ")
    else:
        print("Intruder.!!!")
