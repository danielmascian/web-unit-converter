from flask import Flask,render_template,request,url_for,redirect,session,flash

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("index.html")

@app.route("/length",methods=["GET","POST"])
def length():
    if request.method == "POST":
        value = request.form["value"]
        metric_from = request.form["metric-from"]
        metric_to = request.form["metric-to"]
    return render_template("length.html")

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")


def calculate_length(value,metric_from,metric_to):
    length_units = {
        "km": 1000,
        "m" :  1,
        "cm": 0.01,
        'mm': 0.001
    }

if __name__ == "__main__":
    app.run(debug=True)
