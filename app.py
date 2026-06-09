from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def home():

    password = None
    strength = None

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

        history.append(password)

        score = 0

        if length >= 8:
            score += 1

        if "uppercase" in request.form:
            score += 1

        if "numbers" in request.form:
            score += 1

        if "symbols" in request.form:
            score += 1

        if score <= 2:
            strength = "Weak"
        elif score == 3:
            strength = "Medium"
        else:
            strength = "Strong"

    return render_template(
        "index.html",
        password=password,
        strength=strength,
        history=history
    )

if __name__ == "__main__":
    app.run(debug=True)