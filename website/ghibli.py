from flask import Flask
from flask import Blueprint

ghibli = Blueprint('ghibli', __name__)

@ghibli.route('/ghibli/en')
def Ghibli():
    return "<p>Ghibli</p>"

