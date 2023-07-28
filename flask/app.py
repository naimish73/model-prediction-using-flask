from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from sklearn.preprocessing import StandardScaler
from pipeline.predict_pipeline import PredictPipeline,CustomData

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data=CustomData(
            chargeTime=request.form.get('chargeTime'),
            dischargeTime=request.form.get('dischargeTime')
        )
        pred_df=data.get_data_as_data_frame()
        print(pred_df)
        predict_pipeline = PredictPipeline()   
        results = predict_pipeline.predict(pred_df)
        return render_template('home.html', results=results[0])
    
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)