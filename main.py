from flask import Flask,render_template,request,url_for,redirect,session,flash

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/length")
def length():
    return render_template("length.html")

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

if __name__ == "__main__":
    app.run(debug=True)
