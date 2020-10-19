# This work is licensed under GPLv3.   
# Created by: Rio Akbar, Calvin Nguyen, Erik Stefan, James Tarrant, Dylan Turner

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    AZURE_TOKEN = os.environ.get('AZURE_TOKEN')
    COMPONENT = os.environ.get('AZURE_COMPONENT')
