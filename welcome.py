# this is welcome page. 
from flask import Blueprint


welcome = Blueprint('welcome', __name__) # Blueprint for welcome page. Later this blueprint will be imported by flask app.
@welcome.route('/')
def homepage():
    
    
    return "WELCOME! Go to /dashboard route and type your adress as an endpoint"
