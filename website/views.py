from flask import Flask
from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("Start.html")

@views.route('/en')
def englishhome():
    return render_template("Enghome.html")

@views.route('/choose/en')
def englishchoose():
    return render_template("Engchoose.html")

@views.route('/choose/hi')
def hindichoose():
    return render_template("Hichoose.html")

@views.route('/hi')
def hindihome():
    return render_template("Hihome.html")

