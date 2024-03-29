
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
	    source_port = float(request.form['source_port'])
            destination_port = float(request.form['destination_port'])
            nat_source_port = float(request.form['nat_source_port'])
            nat_destination_port = float(request.form['nat_destination_port'])
            bytes1 = float(request.form['bytes1'])
	    bytes_sent = float(request.form['bytes_sent'])	
	    bytes_received = float(request.form['bytes_received'])
	    packets = float(request.form['packets'])
	    elapsed_time_sec = float(request.form['elapsed_time_sec'])
	    pkts_sent = float(request.form['pkts_sent'])
            pkts_received = float(request.form['pkts_received'])

            prediction=model.predict([[source_port,destination_port,nat_source_port,nat_destination_port,bytes1,bytes_sent,bytes_received,packets,elapsed_time_sec,pkts_sent,pkts_received]])
            output=int(prediction)
            if prediction == 0:
		    return render_template('results.html',prediction_text="allow")
            if prediction == 1:
		    return render_template('results.html',prediction_text="deny")
	    if prediction == 2:
		    return render_template('results.html',prediction_text="drop")
	    if prediction == 3:
		    return render_template('results.html',prediction_text="reset-both")
    else:
        return render_template('results.html')


if __name__=="__main__":
    app.run(debug=True)
	
	
