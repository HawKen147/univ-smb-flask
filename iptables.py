from flask import Flask, redirect, url_for, render_template, request, session
import json
import base64

app = Flask(__name__)
app.debug = True
app.secret_key = 'any'


@app.route("/")
def index():
    if check_user_registered():
        return render_template("index.html")
    else :
        return render_template('autentification.html')
    

@app.route("/start")
def index_html():
    if check_user_registered():
        return render_template("index.html")
    else :
        return render_template('autentification.html')


@app.route("/alias")
def Alias():
    if check_user_registered():
        return render_template("Alias.html")
    else :
        return render_template('autentification.html')


@app.route("/rules_filter")
def rules_filter():
    if check_user_registered():
        return render_template("nat.html")
    else :
        return render_template('autentification.html')


@app.route("/rules_nat_add")
def rules_nat_add():
    if check_user_registered():
        return render_template("ajouter_nat.html")
    else :
        return render_template('autentification.html')


@app.route("/autentification", methods=['POST'])
def autentification():
    result = request.form
    login = result['login']
    password = result['password']
    if check_autentification(login, password):
        return render_template("index.html")
    else:
        return render_template("autentification.html")

@app.route('/alias_json')
def data():
    with open('static/alias.json', 'r') as f:
        data = json.load(f)
    return data


@app.route("/disconnect")
def disconnect():
    session.clear()
    return index()


def check_autentification(login,password):
    password = base64.b64encode(password.encode())
    res = is_in_the_id_folder(login)  #get the line where the login is, false if it is not in the file
    print(res)
    if res :
        print(res)
        if password:
            session['login'] = login
            print('session',session['login'])
            return True
        else:
            return False
    else:
        return False


#check if the user is in the folder
#return his log + pw
def is_in_the_id_folder(login):
    with open('identifiant.txt') as temp_f:
        datafile = temp_f.readlines()
    for line in datafile:
        if login in line:
            return line
    return False  


#check if the session exist
def check_user_registered():
    if 'login' in session:
        return True
    else:
        return False


#add user if doesnt exist
def add_user_files(login,password):
    fichier = open('identifiant.txt', 'a')
    password = base64.b64encode(password.encode())
    fichier.write(str(login) + ':' + str(password))
    fichier.close()
