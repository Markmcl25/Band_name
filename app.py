# Import necessary modules from Flask
from flask import Flask, render_template, request
# Import Colorama for styling text in the terminal (not necessary for web app, but it’s included if you want to use it for local testing)
from colorama import init, Fore, Style

# Initialize the Flask application
app = Flask(__name__)

# Initialize colorama (for terminal output styling, optional)
init()


# Define the home route, this will be triggered when the user visits the root URL '/'
@app.route("/", methods=["GET", "POST"])
def home():
    # Check if the form is submitted with a POST request
    if request.method == "POST":
        # Retrieve the city and pet name from the form inputs
        city = request.form["city"]
        pet = request.form["pet"]
        # Generate the band name by combining the city and pet name
        band_name = f"{city} {pet}"
        # Return the HTML page, passing the generated band name and user inputs to it
        return render_template("index.html", band_name=band_name, city=city, pet=pet)

    # If the page is accessed via GET (the user hasn't submitted the form yet), just render the form without band name
    return render_template("index.html", band_name=None)


# Check if the script is being executed directly (not imported as a module)
if __name__ == "__main__":
    # Start the Flask development server in debug mode (useful during development)
    app.run(debug=True)
