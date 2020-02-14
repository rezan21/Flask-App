from flask import Flask, render_template, url_for, flash, redirect
from forms import RegisterationForm, LoginForm
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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}.','success')
        return redirect(url_for('home'))
    return render_template('register.html',title="Register",form=form)

if __name__ == "__main__":
    app.run(debug=True)