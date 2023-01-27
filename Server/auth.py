from flask import Blueprint, render_template, request, flash, redirect
import random
from .data import log_in
from . import db
import datetime

auth = Blueprint(
    'auth',
    __name__
)


def confirm_password(email, password):
    correct_password = log_in(email)
    confirmation = False
    if password == correct_password:
        confirmation = True
    return confirmation


@auth.route("/login", methods=["GET", "POST"])
def Login():
    if request.method == "POST":
        data = request.form
        name = data.get("FirstName")
        email = data.get("email")
        password = data.get("password")
        x = confirm_password(email, password)
        if x == True:
            return redirect("http://127.0.0.1:5000/logged-in", code=302)
        else:
            flash("Sorry Wrong Password Please Try Again", category='error')
            return render_template("login.html", text="testing")
    elif request.method == "GET":
        return render_template("login.html", text="testing")


@auth.route("/logged-in", methods=["GET", "POST"])
def Logged_in():
    if request.method == "GET":
        return render_template("logged_in.html")
    if request.method == "POST":
        name = request.form.get("Name")
        roomtype = request.form.get("roomtype")
        flash("Customer Checked-in ", category='success')
        room = db.Check_in(name, roomtype)
        return render_template("Customer.html", room=room)


@auth.route("/logout")
def Logout():
    return render_template("logout.html")


@auth.route("/check-out", methods=["GET", "POST"])
def check_out():
    checkout_time = datetime.datetime.now()
    if request.method == "POST":

        name=request.form.get("Name")
        global room
        room = request.form.get("roomnumber")
        (name,room,roomtype, check_in_time) = db.display_details(room)
        amount_dict = {"SEA_FACING":3000, "GARDEN_VIEW":2000, "POOL_VIEW":1000, "SUITE":4000}
        checkout_time = datetime.datetime.strptime(str(checkout_time), '%Y-%m-%d %H:%M:%S.%f')
        check_in_time = datetime.datetime.strptime(str(check_in_time), '%Y-%m-%d %H:%M:%S.%f')
        days = checkout_time - check_in_time
        try:
            days = days.days
        except:
            days = 0
        amount = amount_dict[roomtype]*days
        return render_template("Details.html", Name=name, room=room, roomtype=roomtype, check_in_time=check_in_time, check_out_time=checkout_time,
                            amount=amount)

        flash("No room found Please Try Again", category='error')
        return render_template("check-out.html")
    else:
        return render_template("check-out.html")

room = 0
@auth.route("/checkedout")
def show():
    db.Check_out(room)
    return render_template("checkedout.html", room=room)
