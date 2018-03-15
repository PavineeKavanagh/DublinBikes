from dublinbikes import app
from flask import Flask, render_template, url_for

# route() decorator tells Flask what URL should trigger our function
@app.route('/') 
def main():
    returnDict = {}
    returnDict['user'] = 'Elena'
    returnDict['title'] = 'Dublin Bikes'
    return render_template("index.html", **returnDict)

@app.route('/stationmap')
def stationmap():
    return 'The Station Map page'

@app.route('/predict')
def predict():
    return 'The Predict page'

with app.test_request_context():
    print(url_for('main'))
    print(url_for('stationmap'))