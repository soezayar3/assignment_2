import flask
from flask import Flask, request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

with open('records.json', 'r') as f:
    candidates = json.load(f)

candidates_by_constituency = {}
for candidate in candidates:
    constituency = candidate['constituency']
    if constituency in candidates_by_constituency:
        candidates_by_constituency[constituency].append(candidate)
    else:
        candidates_by_constituency[constituency] = [candidate]

@app.route('/candidates', methods=['GET'])
def api_filter():
    constituency = request.args.get('constituency')
    return jsonify(candidates_by_constituency[constituency])

app.run()