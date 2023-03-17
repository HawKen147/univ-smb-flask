from flask import Flask, redirect, url_for, render_template, request, session
import json
import base64

app = Flask(__name__)
app.secret_key = 'any'

@app.route("/")
def index():
    if check_user_registered():
        return render_template("index.html")
    else :
        return render_template('autentification.html')
    


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

@app.route("/autentification", methods=['POST'])
def autentification():
    result = request.form
    login = result['login']
    password = result['password']
    if check_autentification(login, password):
        return render_template("index.html", prenom=login, nom=password)
    else:
        return render_template("index.html", prenom=login, nom=password)


def nb_row_in_json(file_name):
    with open(file_name,'r') as file:   
        data = json.load(file) 
    print(len(data))
    return len(data)


def check_autentification(login,password):
    password = base64.b64encode(password.encode())
    res = is_in_the_id_folder(login)  #get the line where the login is, false if it is not in the file
    if res :
        password_file = get_password_file(res)
        if password == password_file:
            session['login'] = login
            return True
    #else:
        #on ecrit retourne une erreur
    return True

#check if the user is in the folder*
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
    return False

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



def return_table_td_tr ():
    return render_template("alias_table.html")


