import sys
import pandas as pd
from utils import CustomException
from utils import load_object


class PredictPipeline:
    def __init__(self):
        pass
    
    def predict(self, features):
        try:
            model_path='models\model.pkl'
            model = load_object(file_path=model_path)
            preds = model.predict(features)
            return preds
        except Exception as e:
            raise CustomException("Error in PredictPipeline.predict", e)

class CustomData:
    def __init__ (self, 
                  chargeTime: float,
                  dischargeTime: float,):
        self.chargeTime = chargeTime
        self.dischargeTime = dischargeTime
    
    def get_data_as_data_frame(self):
        try: 
            custom_data_input_dict = {'chargeTime': [self.chargeTime],
                                 'dischargeTime': [self.dischargeTime]}
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException("Error in CustomData.get_data_as_data_frame", e)