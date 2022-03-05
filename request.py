# -*- coding: utf-8 -*-
"""
@author: TSE
"""

import requests
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from joblib import load
import pickle

def predOut(AvgInc):
    
    

    model = load(r'C:\Users\19xtz51b\filename.joblib') 
    
    prediction = model.predict(AvgInc)
   
    
    
    return prediction
	
	
from flask import Flask, render_template,request
app = Flask(__name__)
#app.config['UPLOAD_FOLDER']=r"C:\Users\19xtz51b\Desktop\CollinsMLBatch20September\Day4\MLMatCNN\static"


@app.route('/')
def home():
    form=request.form
    return render_template('test.html',form=form)
	
@app.route('/hello', methods=['POST'])
def hello():    
    
    #f = request.files['myfile']  
    #f.save(secure_filename(f.filename))
    #f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))         
	
    #predAnimal = os.path.join(app.config['UPLOAD_FOLDER'],f.filename)
    AvgInc=list([request.form['income']])
    NpAvgInc=np.array([AvgInc])
    
    output= predOut(NpAvgInc)
    
    return render_template('test.html',output=output)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
