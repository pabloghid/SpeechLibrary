from flask import Flask, render_template
import requests
import voice_functions

app = Flask(__name__)

@app.route("/")
def home():
    query = "the lord of the rings"
    response = requests.get(f"http://openlibrary.org/search.json?q={query}")
    data = response.json()
    titles = [book['title'] for book in data['docs']]
    return render_template("home.html", titles=titles)

@app.route("/search", methods=["POST"])
def search():
    search_function = voice_functions.VoiceSearch()
    return render_template("search.html", response=search_function)

if __name__ == "__main__":
    app.run(debug=True, threaded=True)