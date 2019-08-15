#!/usr/bin/env python

from flask import Flask, render_template, redirect, url_for, request, session
import pymongo
import bcrypt
from models.User import User

app = Flask(__name__)

# config database
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
users = mydb["user"]

#print all database name exits in mongod database
print(myclient.list_database_names())

#init data
def init_data():
    user = User("Thuy Tony", "thuytony", "123456abcd")
    users.insert_one(user.hashPassword().toJson())

    user2 = User("Admin", "admin", "123456abcd")
    users.insert_one(user2.hashPassword().toJson())

#handle home page, login page and login api
@app.route('/', methods=['GET', 'POST'])
def login():
    error = None
    userSession = None
    if request.method == 'POST':
        if 'user_name' not in request.form or 'password' not in request.form:
            error = 'Please input username and password.'
            return render_template('login.html', error=error)

        if request.form['user_name'] == "" or request.form['password'] == "":
            error = 'Username and password is invalidate'
            return render_template('login.html', error=error)

        login_user = users.find_one({'user_name' : request.form['user_name']})
        if login_user:
            if bcrypt.hashpw(request.form['password'].encode('utf-8'), login_user['password']) == login_user['password']:
                # session['user_name'] = request.form['user_name']
                return render_template('home.html', userSession=login_user['name'])
        error = 'Login failed.'
        return render_template('login.html', error=error)

    if request.method == 'GET':
        return render_template('login.html')

#handle error redirect
@app.errorhandler(404)
def not_found(error):  
    return render_template('404.html')

if __name__ == "__main__":
    app.debug = True
    app.run()