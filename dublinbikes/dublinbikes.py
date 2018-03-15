# -*- coding: utf-8 -*-

import jcd_scrapper
import time
import app
from flask import Flask, render_template



"""Main module."""
def main():
    """ Controls the major elements of the program"""

    # Calling the JCD Scrapper
    jcd_scrapper.main()
    time.sleep(305)

@app.route('/')
def index():
    returnDict = {}
    returnDict['user'] = 'Elena'
    returnDict['title'] = 'Dublin Bikes'
    return 'Index Page!'
