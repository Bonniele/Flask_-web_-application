
from flask import Blueprint
from flask import Flask, render_template


x = Blueprint('home',__name__)
y = Blueprint('statistics',__name__)

@x.route("/")
def home():
    return render_template ("home.html")

@y.route('/statistics')
def statistics():
    return render_template("statistics.html")