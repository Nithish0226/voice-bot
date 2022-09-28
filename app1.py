import re
from flask import Flask, render_template, request,redirect,url_for
from main import *
import json
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index1.html')

@app.route('/model', methods=['POST', 'GET'])
def login():
 if request.method == 'POST':
  user = request.form['nm']
  res = json.loads(user)
  output = response(res)
  return redirect(url_for('output', name=output))
 else:
  user = request.args.get('nm')
  res = json.loads(user)
  output = response(res)
  return redirect(url_for('output', name=output))

if __name__ == '__main__':
   app.run()