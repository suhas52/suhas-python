from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '50d0cd50f5684a670ea87dc663697af1'

posts = [
    {
        'author': 'Corey',
        'title': 'Blog post 1',
        'content': 'First post content',
        'date_posted': 'Apirl 20, 2025'
    },
    {
        'author': 'Adam',
        'title': 'Blog post 2',
        'content': 'Second post content',
        'date_posted': 'Apirl 25, 2025'
    }    

]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template("register.html", title='Registration', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)