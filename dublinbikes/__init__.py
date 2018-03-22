# -*- coding: utf-8 -*-

"""Top-level package for DublinBikes."""

from flask import Flask # ------------------------- import Flask class
app = Flask(__name__) # --------------------------- create instance of this class 'app' (name or main?)
from dublinbikes import dublinbikes # ------------- Local Package

# from flask_bootstrap import Bootstrap # ----------- getting Bootstrap for Flask

# Bootstrap(app) # ---------------------------------- Creating app as a Bootstrap instance



__author__ = """Harsh Gupta"""
__email__ = 'harsh.gupta@ucdconnect.ie'
__version__ = '0.1.0'


