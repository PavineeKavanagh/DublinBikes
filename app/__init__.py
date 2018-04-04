# -*- coding: utf-8 -*-

"""Top-level package for DublinBikes."""

from flask import Flask # ------------------------- import Flask class
app = Flask(__name__) # --------------------------- create instance of this class 'app' (name or main?)
app.debug=False
from app import dublinbikes # ------------- Local Package



