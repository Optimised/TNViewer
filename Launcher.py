#! /usr/bin/python
import sys
import json
from flask import Flask, render_template
import TemporalNetwork as tn

app = Flask(__name__)

@app.route("/data")
def data():
	f = open("data.txt")
	t = tn.readFile(f)
	return json.dumps(getData(t))

@app.route('/static/<path:filename>')
def serve_static(filename):
    root_dir = os.path.dirname(os.getcwd())
    return send_from_directory(os.path.join(root_dir, 'static'), filename)

@app.route("/")
def index():
	"""
	When you request the root path, you'll get the index.html template.
	"""
	return render_template("index.html")

def getData(tn):
	data = {"nodes" : [],
			"links": []}

	_id = 0
	for n in tn.nodes:
		data["nodes"].append({	"id" : n.name,
								"group" : _id})
		_id+=1

	for l in tn.links:
		data["links"].append({	"source": l.n1.name, 
								"target": l.n2.name, 
								"value": l.constraint})
	return data

if __name__ == "__main__":
	app.run()
 