from flask import Flask
from flask import Blueprint

vfb = Blueprint('vfb', __name__)

@vfb.route('/vfb/en')
def Ghibli():
    return "<p>Video for Bride</p>"

