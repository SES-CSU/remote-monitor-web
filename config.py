# This work is licensed under the Creative Commons Attribution-NonCommercial 3.0 Australia License.  
# Created by: Rio Akbar, Calvin Nguyen, Erik Stefan, James Tarrant, Dylan Turner

import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    AZURE_TOKEN = os.environ.get('AZURE_TOKEN')
    COMPONENT = os.environ.get('AZURE_COMPONENT')
