from flask import Flask,request,jsonify
import numpy as np
import pickle

model = pickle.load(open('maliyet.pkl','rb'))
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])    
def predict():
    akma = request.form.get('akma')
    cekme = request.form.get('cekme')
    acinim = request.form.get('acinim')
    input_query = np.array([[akma,cekme,acinim]])
    result = model.predict(input_query)[0]
    return jsonify({'placement':str(result)})
if __name__ == '__main__':
    app.run(debug=True)
