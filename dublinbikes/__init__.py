# -*- coding: utf-8 -*-

"""Top-level package for DublinBikes."""

from flask import Flask # ------------------------- import Flask class
app = Flask(__name__) # --------------------------- create instance of this class 'app' (name or main?)
from dublinbikes import flaskdb


__author__ = """Harsh Gupta"""
__email__ = 'harsh.gupta@ucdconnect.ie'
__version__ = '0.1.0'


