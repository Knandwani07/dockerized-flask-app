from flask import Flask, render_template
import os

app = Flask(__name__)

VISITS_FILE = "visits.txt"

@app.route('/')
def home():

    if not os.path.exists(VISITS_FILE):
        with open(VISITS_FILE, "w") as f:
            f.write("0")

    with open(VISITS_FILE, "r") as f:
        visits = int(f.read())

    visits += 1

    with open(VISITS_FILE, "w") as f:
        f.write(str(visits))

    message = os.getenv(
        "APP_MESSAGE",
        "Welcome to my Dockerized Flask Application"
    )

    return render_template(
        "index.html",
        visits=visits,
        message=message
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
