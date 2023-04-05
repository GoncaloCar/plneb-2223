from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template('home.html', title= "Welcome")

@app.route("/Engenharia")
def engenharia():
    return render_template("engenharia.html")

@app.route("/Égua")
def égua():
    return render_template("égua.html")

@app.route("/Elefante")
def elefante():
    return render_template("elefante.html")



app.run(host="localhost", port=4002, debug = True)



###TPC: Engernharia, égua, elefante