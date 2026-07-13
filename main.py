from flask import Flask,render_template,request,url_for,redirect,session,flash

app = Flask(__name__)
app.secret_key = "my-key"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/length",methods=["GET","POST"])
def length():
    result = None
    value = None
    metric_from = None
    metric_to = None

    if request.method == "POST":
        value = float(request.form["value"])
        session["length_value"] = value
        metric_from = request.form["metric_from"]
        metric_to = request.form["metric_to"]
        result = calculate_length(value, metric_from, metric_to)
        return render_template("length_result.html", result = result , value = value , metric_from = metric_from , metric_to = metric_to,back_page = "length")
    return render_template("length.html",value=session.get("length_value"))

@app.route("/weight",methods=["GET","POST"])
def weight():
    result = None
    value = None
    metric_from = None
    metric_to = None

    if request.method == "POST":
        value = float(request.form["value"])
        metric_from = request.form["metric_from"]
        metric_to = request.form["metric_to"]
        session["weight_value"] = value
        result = calculate_weight(value, metric_from, metric_to)
        return render_template("weight_result.html", result = result , value = value , metric_from = metric_from , metric_to = metric_to,back_page = "weight")
    return render_template("weight.html" , value=session.get("weight_value"))

@app.route("/temperature",methods=["GET","POST"])
def temperature():
    result = None
    value = None
    metric_from = None
    metric_to = None
    if request.method == "POST":
        value = float(request.form["value"])
        metric_from = request.form["metric_from"]
        metric_to = request.form["metric_to"]
        session["temperature_value"] = value
        result = calculate_temperature(value, metric_from, metric_to)
        return render_template("temperature_result.html", result = result , value = value , metric_from = metric_from , metric_to = metric_to,back_page = "temperature")
    return render_template("temperature.html",value=session.get("temperature_value"))


def calculate_length(value,metric_from,metric_to):
    length_units = {
        "km": 1000,
        "m" : 1,
        "cm": 0.01,
        'mm': 0.001
    }
    meters = value * length_units[metric_from]
    rezult = meters / length_units[metric_to]
    return rezult

def calculate_weight(value,metric_from,metric_to):
    weight_units = {
        "kg": 1000,
        "g" : 1,
        "mg": 0.01,
        "t": 1_000_000
    }
    gram = value * weight_units[metric_from]
    rezult = gram / weight_units[metric_to]
    return rezult

def calculate_temperature(value, metric_from, metric_to):
    if metric_from == metric_to:
        return value

    if metric_from == "c":
        if metric_to == "f":
            return (value * 9 / 5) + 32
        elif metric_to == "k":
            return value + 273.15

    elif metric_from == "f":
        if metric_to == "c":
            return (value - 32) * 5 / 9
        elif metric_to == "k":
            return (value - 32) * 5 / 9 + 273.15

    elif metric_from == "k":
        if metric_to == "c":
            return value - 273.15
        elif metric_to == "f":
            return (value - 273.15) * 9 / 5 + 32

if __name__ == "__main__":
    app.run(debug=True)
