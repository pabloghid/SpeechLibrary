from flask import Flask, render_template
import requests
import voice_functions

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/search/<type>", methods=["POST"])
def search(type):
    match type:
        case 'books':
            search_function = voice_functions.search_book()
        case 'authors':
            search_function = voice_functions.search_author()
    
    return render_template("search.html", response=search_function)


if __name__ == "__main__":
    app.run(debug=True, threaded=True)