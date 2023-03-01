from flask import Flask, request

app = Flask(__name__)

user_details = {}

user_details["katie"] = {"email": "b@b.com", "password": "katie"}
user_details["david"] = {"email": "a@a.com", "password": "david"}
user_details["yul"] = {"email": "c@c.com", "password": "yul"}


@app.route('/login', methods=['POST'])
def login():
    page = ""
    form = request.form
    if form["username"] in user_details.keys():
        new_dict = user_details[form["username"]]
        if form["email"] == new_dict["email"] and form["password"] == new_dict["password"]:
            page += "Login successful"
        else:
            page += "Login failed. Email or password incorrect!"
    else:
        page += "Username incorrect / User not found!"

    return page


@app.route('/')
def index():
    page = ""
    f = open(
        "C:/Users/user/Documents/Replit 100 Days Of Code/Python/Day79.html", "r")
    page = f.read()
    f.close()

    page = page.replace("Document", "Login Form")
    return page


app.run(host='0.0.0.0', port=5500)
