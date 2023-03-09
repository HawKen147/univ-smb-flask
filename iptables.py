# save this as app.py
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def index_html():
    return render_template("index.html")

@app.route("/alias")
def Alias():
    return render_template("Alias.html")

@app.route("/rules_filter")
def rules_filter():
    return render_template("nat.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("ajouter_nat.html")
