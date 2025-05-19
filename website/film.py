from flask import Flask
from flask import Blueprint

film = Blueprint('film', __name__)

@film.route('/film/en')
def Film():
    return "<p>Video for Bride</p>"

