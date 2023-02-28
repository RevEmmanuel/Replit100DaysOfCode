from flask import Flask

app = Flask(__name__)

my_reflections = {}

my_reflections["78"] = {"link": "https://github.com/RevEmmanuel/Replit100DaysOfCode/tree/main/Python/Day78",
                       "Reflection": "Was actually quite easy for me ven if I was a bit lazy with the css 😭"}

my_reflections["79"] = {
    "link": "https://github.com/RevEmmanuel/Replit100DaysOfCode/blob/main/Python/Day79.py", "Reflection": "Very very easy."}


@app.route('/<pageNumber>')
def index(pageNumber):
    global Reflections
    page = ""
    f = open("reflection.html", "r")
    page = f.read()
    f.close()

    page = page.replace("{day}", pageNumber)
    page = page.replace("{date}", my_reflections[pageNumber]["link"])
    page = page.replace(
        "{reflection}", my_reflections[pageNumber]["Reflection"])
    return page


app.run(host='0.0.0.0', port=5500)
