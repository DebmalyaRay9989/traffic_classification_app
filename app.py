
from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    output=0
    prediction=0
    if request.method == 'POST':
	source_port = int(request.form['source_port'])
        destination_port = int(request.form['destination_port'])
        nat_source_port = int(request.form['nat_source_port'])
        nat_destination_port = int(request.form['nat_destination_port'])
        bytes1 = int(request.form['bytes1'])
	bytes_sent = int(request.form['bytes_sent'])	
	bytes_received = int(request.form['bytes_received'])
	packets = int(request.form['packets'])
	elapsed_time_sec = int(request.form['elapsed_time_sec'])
	pkts_sent = int(request.int['pkts_sent'])
        pkts_received = int(request.form['pkts_received'])

        prediction=model.predict([[source_port,destination_port,nat_source_port,nat_destination_port,bytes1,bytes_sent,bytes_received,packets,elapsed_time_sec,pkts_sent,pkts_received]])
        output=int(prediction)

        if output == 0:
	    return render_template('results.html',prediction_text="allow")
        if output == 1:
	    return render_template('results.html',prediction_text="deny")
	if output == 2:
	    return render_template('results.html',prediction_text="drop")
	if output == 3:
	    return render_template('results.html',prediction_text="reset-both")
    else:
        return render_template('results.html')


if __name__=="__main__":
    app.run(debug=True)
	
	
