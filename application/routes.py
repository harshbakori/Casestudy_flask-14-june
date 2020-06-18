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

@app.route("/CreateAccount")
def CreateAccount():
    form = RegisterForm()
    return render_template("CreateAccount.html",form=form,home=True)

@app.route("/CustomerStatus")
def CustomerStatus():
    return render_template("CustomerStatus.html",home=True)

@app.route("/DepositMoney")
def DepositMoney():
    return render_template("DepositMoney.html",home=True)

@app.route("/TransferMoney")
def TransferMoney():
    return render_template("TransferMoney.html",home=True)

@app.route("/UpdateCustomer")
def UpdateCustomer():
    return render_template("UpdateCustomer.html",home=True)

@app.route("/WithdrawAmount")
def WithdrawAmount():
    return render_template("WithdrawAmount.html",home=True)

@app.route("/Login")
def Login():
    return render_template("Login.html",home=True)


