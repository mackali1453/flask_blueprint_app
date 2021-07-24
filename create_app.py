# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 19:10:33 2021

@author: melik
"""


from flask import Flask
from distance import dashboard
from welcome import welcome
app = Flask(__name__)
app.register_blueprint(dashboard)
app.register_blueprint(welcome)
if __name__=="__main__":
    app.run(host='0.0.0.0')

