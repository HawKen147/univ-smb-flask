from flask import Flask, redirect, url_for, render_template, request

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
