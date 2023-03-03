from flask import Flask, redirect, request

user_list = []
try:
    with open("Day84UserLogin", "x") as file:
        file = open("Day84UserLogin", "r")
        data = file.read()
        user_list = eval(data)
        file.close()
except FileExistsError:
    with open("Day84UserLogin", "r") as file:
        data = file.read()
        user_list = eval(data)
        file.close()

app = Flask(__name__)


@app.route("/signup", methods=["POST"])
def createUser():
    keys = []
    for value in user_list:
        keys.append(value["username"])
    form = request.form
    if form["username"] not in keys:
        new_dict = {"username": form["username"],
                    "name": form["name"], "password": form["password"]}
        user_list.append(new_dict)
        return redirect("/login")
    else:
        return redirect("/signup")


def find_old_dict(username):
    dict = {}
    for k in user_list:
        if k["username"] == username:
            return k
    return {}


@app.route("/login", methods=["POST"])
def doLogin():
    keys = []
    for value in user_list:
        keys.append(value["username"])
    form = request.form
    if form["username"] not in keys:
        return redirect("/login")
    else:
        old_dict = find_old_dict(form["username"])
        if form["password"] == old_dict["password"]:
            return f"""Hello {old_dict["name"]}"""
        else:
            return redirect("/login")


@app.route("/login")
def login():
    page = ""
    f = open("login.html", "r")
    page = f.read()
    f.close()
    return page


@app.route("/signup")
def signup():
    page = ""
    f = open("signup.html", "r")
    page = f.read()
    f.close()
    return page


@app.route('/')
def index():
    page = """<p><a href="/signup">Sign up</a></p>
    <p><a href="/login">Log in</a></p>"""
    return page


app.run(host='0.0.0.0', port=5000)
