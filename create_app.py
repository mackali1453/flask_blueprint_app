# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:10:33 2021

@author: melik
"""


from flask import Flask 
#importing blueprints
from distance import dashboard
from welcome import welcome
app = Flask(__name__)
#registering blueprints to app
app.register_blueprint(dashboard)
app.register_blueprint(welcome)
if __name__=="__main__":
    app.run(host='0.0.0.0') # we bind '0.0.0.0' to let docker container to be accessible from localhost

