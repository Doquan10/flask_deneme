from flask import Flask,request,jsonify
import numpy as np
import pickle
model = pickle.load(open('model.sav','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"