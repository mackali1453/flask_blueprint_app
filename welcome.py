from flask import Blueprint


welcome = Blueprint('welcome', __name__)
@welcome.route('/')
def homepage():
    
    
    return "WELCOME! Go to /dashboard route and type your adress as an endpoint"
