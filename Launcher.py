#! /usr/bin/python
import sys
import json
from flask import Flask, render_template
import TemporalNetwork as TN

app = Flask(__name__)

@app.route("/data")
def data():
	f = open("p06.tn")
	t = TN.readFile(f)
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
			"edges": []}

	_id = 0
	for n in tn.nodes:
		data["nodes"].append({	"id" : n.name,
								"group" : tn.getID(n.name)})
		_id+=1

	for l in tn.links:
		data["edges"].append({	"source": tn.nodes.index(l.n1), 
								"target": tn.nodes.index(l.n2), 
								"value": l.constraint})
	return data

def getGraphVizData(tn):
	print "digraph G {"

	for c in tn.getNodeClusters():
		


if __name__ == "__main__":
	# app.run("0.0.0.0", 5000)

	f = open("p06.tn")
	t = TN.readFile(f)
	print getGraphVizData(t)
 