from flask import Blueprint, render_template, request, redirect, url_for, flash
from .extensions import db
from .models import Message

my_app = Blueprint("my_app", __name__)

@my_app.route("/")
def index():
    return render_template("index.html")

@my_app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@my_app.route("/email", methods=["POST"])
def email():
    input_field = request.form['input_field']
    email = request.form['email']
    message = request.form['message']
    input_form = Message(input_field=input_field, email=email, message=message)    
    db.session.add(input_form) 
    db.session.commit()
    flash('Message send successful', "success")
    #return ('', 204) 
    return redirect(url_for('my_app.index'))
 
