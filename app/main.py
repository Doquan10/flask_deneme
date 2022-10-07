from flask import Flask,request,jsonify
import numpy as np
import pickle
import pandas as pd
import joblib
app = Flask(__name__)
@app.route('/')
def index():
    return "Hello world"
@app.route('/predict',methods=['POST'])    
def predict():
    df = pd.DataFrame(columns=['OPERASYON SAYISI','KAMLI DELİK','ZORLUK KATSAYISI','TOPLAM AĞIRLIK',
                           'KALIP TİPİ_0','KALIP TİPİ_1','KALIP TİPİ_2','KALIP TİPİ_3'])


    operasyon_sayisi=request.form.get('akma')
    kamli_delik=request.form.get('cekme')
    zorluk_katsayisi=2
    toplam_agirlik=request.form.get('acinim')
    kalip_tipi0=0
    kalip_tipi1=1
    kalip_tipi2=0
    kalip_tipi3=3
 
    df2 = df.append({'OPERASYON SAYISI' : operasyon_sayisi, 'KAMLI DELİK' : kamli_delik,'ZORLUK KATSAYISI'=zorluk_katsayisi, 'TOPLAM AĞIRLIK' : toplam_agirlik,
                'KALIP TİPİ_0' : kalip_tipi0, 'KALIP TİPİ_1' : kalip_tipi1, 'KALIP TİPİ_2' : kalip_tipi2, 'KALIP TİPİ_3' : kalip_tipi3}, ignore_index = True)



    filename = 'xgb.pkl'
    loaded_model = joblib.load(filename)
    result = loaded_model.predict(df2)
    return jsonify({'placement':str(result)})
    #print(result)
if __name__ == '__main__':
    app.run(debug=True)
