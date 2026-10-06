from flask import Flask, render_template, request

# initialize the Flask application
app = Flask(__name__, template_folder='template')

# define routes
@app.route('/')
def home():
    return "Web Development in Python"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello, {name}!"

@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"The sum of {a} and {b} is {a + b}"

@app.route("/template")
def template():
    return render_template("index.html", name= "Pratyush")

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name")
        return f"Form submitted for {name}!"
    return render_template("form.html")

@app.route('/page-form')
def page_form():
 return render_template("page-form.html")
    

# run the application
if __name__ == '__main__':
    app.run(debug=True)