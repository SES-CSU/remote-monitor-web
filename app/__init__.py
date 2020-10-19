# This work is licensed under Firmware: GPLv3.   
# Created by: Rio Akbar, Calvin Nguyen, Erik Stefan, James Tarrant, Dylan Turner

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)

from app import routes