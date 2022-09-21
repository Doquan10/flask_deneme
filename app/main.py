from flask import Flask
import pickle

model = pickle.load(open('model.sav','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"