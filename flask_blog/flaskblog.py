from flask import Flask, render_template
app = Flask(__name__)

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


if __name__ == '__main__':
    app.run(debug=True)