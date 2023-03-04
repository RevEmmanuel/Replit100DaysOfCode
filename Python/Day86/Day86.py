from flask import Flask, redirect, session, request, os

app = Flask(__name__)
static_url_path = "/static"
app.secret_key = os.environ['session_key']
user_list = {"username": "adeola", "password": "mypassword1"}
entries_list = []

try:
    with open("entries", "x") as file:
        file = open("entries", "r")
        data = file.read()
        entries_list = eval(data)
        file.close()
except FileExistsError:
    with open("entries", "r") as file:
        data = file.read()
        entries_list = eval(data)
        file.close()


@app.route('/')
def index():
    if session.get("user"):
        return redirect("/edit")
    page = ""
    f = open("blog.html", "r")
    page = f.read()
    f.close()
    page = page.replace("{content}", getBlogs())
    return page


@app.route('/login_page')
def login_page():
    if session.get("user"):
        return redirect("/edit")
    page = ""
    f = open("login.html", "r")
    page = f.read()
    f.close()
    return page


def getBlogs():
    entry = ""
    f = open("entry.html", "r")
    entry = f.read()
    f.close()
    keys = entries_list.keys()
    keys = list(keys)
    content = ""
    for key in reversed(keys):
        this_entry = entry
        if key != "user":
            this_entry = this_entry.replace(
                "{title}", entries_list[key]["title"])
            this_entry = this_entry.replace(
                "{date}", entries_list[key]["date"])
            this_entry = this_entry.replace(
                "{body}", entries_list[key]["body"])
            content += this_entry
    return content


@app.route('/login', methods=["POST"])
def login():
    if session.get("user"):
        return redirect("/edit")
    form = request.form
    if form["username"] == user_list["username"] and form["password"] == user_list["password"]:
        session["user"] = True
        return redirect("/edit")
    else:
        return redirect("/login_form")


@app.route("/edit")
def edit():
    if not session.get("user"):
        return redirect("/")
    page = ""
    f = open("edit.html", "r")
    page = f.read()
    page = page.replace("{content}", getBlogs())
    f.close()
    return page


@app.route("/add", methods=["POST"])
def add():
    form = request.form
    entry = {"title": form["title"],
             "date": form["date"], "body": form["body"]}
    entries_list.append(entry)
    return redirect("/edit")


@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")


app.run(host='0.0.0.0', port=5500)
