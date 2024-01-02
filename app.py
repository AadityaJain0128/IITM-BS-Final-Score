from flask import Flask, render_template, redirect, request
from final_score import score_calc, python_calc

app = Flask(__name__)
# app.config["SECRET_KEY"] = "a"

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        if request.form.get("score"):
            return redirect("score")
        else:
            return redirect("python")
    return render_template("index.html")


@app.route("/python", methods=['GET', 'POST'])
def python():
    if request.method == "POST":
        gaa = float(request.form.get("gaa"))
        qz1 = float(request.form.get("qz1"))
        oppe1 = float(request.form.get("oppe1"))
        oppe2 = float(request.form.get("oppe2"))
        wta = float(request.form.get("wta"))
        message, F, colour = python_calc(gaa, qz1, oppe1, oppe2, wta)
        return render_template("/python.html", msg=message, colour=colour, F=F, qz1=qz1, oppe1=oppe1, oppe2=oppe2, wta=wta, gaa=gaa)
    return render_template("/python.html")


@app.route("/score", methods=['GET', 'POST'])
def score():
    if request.method == "POST":
        gaa = float(request.form.get("gaa"))
        qz1 = float(request.form.get("qz1"))
        qz2 = float(request.form.get("qz2"))
        message, F, colour = score_calc(gaa, qz1, qz2)
        return render_template("/score.html", msg=message, colour=colour, F=F, qz1=qz1, qz2=qz2, gaa=gaa)
    return render_template("/score.html")
 

if __name__ == "__main__":
    app.run(debug=True)