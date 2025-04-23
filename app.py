from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    # Define the questions that will be displayed on the webpage
    question_city = "Which city did you grow up in?"
    question_pet = "What is the name of a pet?"

    # When the form is submitted, retrieve the answers
    if request.method == "POST":
        city = request.form["city"]
        pet = request.form["pet"]
        # Generate the band name by combining city and pet name
        band_name = f"{city} {pet}"
        return render_template("index.html", band_name=band_name, city=city, pet=pet,
                               question_city=question_city, question_pet=question_pet)

    # Render the page with the questions and without the band name yet
    return render_template("index.html", band_name=None, question_city=question_city, question_pet=question_pet)


if __name__ == "__main__":
    app.run(debug=True)
