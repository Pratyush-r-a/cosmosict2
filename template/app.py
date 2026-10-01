from flask import Flask



app = Flask(__name__)

@app.route('/')
def home():
    return " web development python"

@app.route("/greet/<name>")                                                                                                                                                                                                           
def greet(name):
    return f"hello, {name}!"
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    return f"{a}+{b} = {a + b}"
@app.route("/sub/<int:a>/<int:b>")
def sub(a,b):
    return f"{a}-{b} = {a - b}"
@app.route("/mul/<int:a>/<int:b>")
def mul(a,b):
    return f"{a}*{b} = {a * b}"
@app.route("/template")
def template():
    return render_template("index.html",name="anita")

if __name__ == "__main__":
    app.run(debug=True)

