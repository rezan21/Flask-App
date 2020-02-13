from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        "author":"rey",
        "title": "the book of the year"
    },
     {
        "author":"naghi",
        "title": "the failure"
    }
]

@app.route("/")
def home():
    return render_template('index.html', posts=posts, title="MAIN")

@app.route("/about")
def about():
    return render_template('about.html', title="ABOUT")


if __name__ == "__main__":
    app.run(debug=True)