from flask import Flask, request

app = Flask(__name__)

user_details = {}

user_details["katie"] = {"email": "b@b.com", "password": "katie"}
user_details["david"] = {"email": "a@a.com", "password": "david"}
user_details["yul"] = {"email": "c@c.com", "password": "yul"}


@app.route('/check', methods=['POST'])
def robot_check():
    form = request.form
    if form['metal'] == "Yes":
        return "You're a robot!"
    elif "error" in form["infinity"].lower():
        return "You're a robot!"
    elif form["food"] == "synthetic oil":
        return "You're a robot!"
    else:
        return "Hi there fellow human"


@app.route('/')
def index():
    page = f"""
<html>
<head>
<title>Robot Test</title>
</head>
<body>
<form method="post" action="/check">

  <p>Are you made of metal? <input type="radio" name="metal" value="Yes"> Yes     <input type="radio" name="metal" value="No"> No </p>

  <p>What is infinity + 1? <input type="text" name="infinity" required></p>

  <p>Which is your favorite food? <select name="food"><option value="human food">Human food</option><option value="synthetic oil">Synthetic Oil</option></select></p>

  <button type="submit">I am not a robot</button>

</form>
</body>
</html>
"""

    return page


app.run(host='0.0.0.0', port=5500)
