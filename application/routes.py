from application import app
from flask import render_template, request, json, jsonify, Response, redirect, flash, url_for, session
from application.forms import RegisterForm,DeleteAccount

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    form = RegisterForm()
    return render_template("CreateAccount.html",form=form,home=True)

@app.route("/Deleteaccount")
def delac():
    form = DeleteAccount()
    return render_template("DeleteAccount.html",form=form)