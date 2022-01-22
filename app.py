from flask import Flask, jsonify
from backend import gethintf, getansf, qdumpf, getqf

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>API Online</h1>'

@app.route('/gethint/<qid>')
def gethint(qid=None):
    print('Gethint called!')
    return jsonify(gethintf(qid))

@app.route('/getans/<qid>')
def getans(qid=None):
    print('Getanswer called!')
    return jsonify(getansf(qid))

# @app.route('/getid/<q>')
# def getid(q=None):
#     print('Getid called!')
#     return jsonify(getidf(q))

@app.route('/qdump/<q>/<a>/<h>')
def qdump(q=None,a=None,h=None):
    print('QDump called!')
    return jsonify(qdumpf(q,a,h))

@app.route('/getq/<qid>')
def getq(qid=None):
  return jsonify(getqf(qid))

app.run(host='0.0.0.0', port=8080)