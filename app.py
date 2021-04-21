from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("first_page.html")

@app.route("/jinja-intro/")
def hello_world_fancy():
    return render_template(
        "jinja_intro.html",
        name="David Tso",
        template_name="Python"
    )

@app.route("/expressions/")
def expressions():
    data = {
        "color": "red",
        "animal_one": "elephant",
        "animal_two": "fox",
        "orange_amount": 20,
        "apple_amount": 39,
        "donate_amount": 45,
        "first_name": "David",
        "last_name": "Tso"
    }

    return render_template("expressions.html", **data)


class Moon:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

@app.route("/data-structures/")
def data_structures():
    
    movies = ["Avengers", "Jumanji", "Godzilla"]

    car = {
        "brand": "Tesla",
        "model": "unknown",
        "year": 2030
    }

    moons = Moon("Alpha", "Beta", "Gamma", "Delta")

    return render_template("data_structures.html", movies=movies, car=car, moons=moons)


@app.route("/conditionals-basics/")
def conditionals_basics():
    company = "Apple"
    return render_template("conditionals_basics.html", company=company)



@app.route("/loops-basics/")
def loops_basics():
    
    user_os = {
        "David": "MacOS",
        "Ricky": "Windows",
        "John": "MacOS"
    }
    
    return render_template("loops_and_conditionals.html", user_os=user_os)
