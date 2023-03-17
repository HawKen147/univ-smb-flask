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
    #nb_row = nb_row_in_json('static/alias.json')
    if check_user_registered():
        return render_template("Alias.html")
    else :
        return render_template('autentification.html')


@app.route("/rules_filter")
def rules_filter():
    return render_template("nat.html")
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


@app.route("/disconnect")
def disconnect():
    session.clear()
    return index()


def check_autentification(login,password):
    password = base64.b64encode(password.encode())
    res = is_in_the_id_folder(login)  #get the line where the login is, false if it is not in the file
    if res :
        password_file = get_password_file(res)
        if password == password_file:
            session['login'].append(str(login))
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
        return 'la variable existe'
    else:
        return 'la variable existe pas'


#get the password in the file
def get_password_file(line):
    nb = line.find(':')
    line = line[nb + 1:-1] #we don't want the ':' char
    return line


#add user if doesnt exist
def add_user_files(login,password):
    fichier = open('identifiant.txt', 'a')
    password = base64.b64encode(password.encode())
    fichier.write(str(login) + ':' + str(password))
    fichier.close()


def nb_row_in_json(file_name):
    with open(file_name,'r') as file:   
        data = json.load(file) 
    return len(data)

