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
            type='book'
        case 'authors':
            search_function = voice_functions.search_author()
            type='author'
            print(search_function)
    
    return render_template("search.html", response=search_function, type=type )

@app.route("/test", methods=["GET"])
def test():
    return render_template("test.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True)