from flask import Flask, redirect, url_for, render_template, request
import json

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/start")
def index_html():
    return render_template("index.html")

@app.route("/alias")
def Alias():
    nb_row = nb_row_in_json('static/alias.json')
    """for i in len(nb_row):
        return_table_td_tr()"""
    return render_template("Alias.html")

@app.route("/rules_filter")
def rules_filter():
    return render_template("nat.html")

@app.route("/rules_nat_add")
def rules_nat_add():
    return render_template("ajouter_nat.html")

def nb_row_in_json(file_name):
    with open(file_name,'r') as file:   
        data = json.load(file) 
    print(len(data))
    return len(data)


def return_table_td_tr ():
    return render_template("alias_table.html")
