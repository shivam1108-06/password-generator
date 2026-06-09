from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    password = None

    if request.method == "POST":

        length = int(request.form["length"])

        characters = string.ascii_lowercase

        if "uppercase" in request.form:
            characters += string.ascii_uppercase

        if "numbers" in request.form:
            characters += string.digits

        if "symbols" in request.form:
            characters += string.punctuation

        password = "".join(
            random.choice(characters)
            for _ in range(length)
        )

    return render_template(
        "index.html",
        password=password
    )

if __name__ == "__main__":
    app.run(debug=True)