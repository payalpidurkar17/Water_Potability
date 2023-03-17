import numpy as np
import pandas as pd
import pickle
import json
import config

class Water_Potability():
    def __init__(self,ph, Hardness, Solids, Chloramines, Conductivity,Organic_carbon,Trihalomethanes,Turbidity):
        self.ph = ph
        self.Hardness = Hardness
        self.Solids = Solids
        self.Chloramines = Chloramines
        self.Conductivity = Conductivity
        self.Organic_carbon = Organic_carbon
        self.Trihalomethanes = Trihalomethanes
        self.Turbidity = Turbidity

    def Load_Model(self):
      with open (config.MODEL_PATH,'rb') as f:
          self.model = pickle.load(f)

      with open(config.JSON_PATH,'r') as f:
          self.json_data = json.load(f)

    def get_status(self):
        self.Load_Model()
        test_array = np.zeros(len([self.ph,self.Hardness,self.Solids,self.Chloramines,self.Conductivity,self.Organic_carbon,
            self.Trihalomethanes,self.Turbidity]))
        print(test_array)
        test_array[0] = self.ph
        test_array[1] = self.Hardness
        test_array[2] = self.Solids
        test_array[3] = self.Chloramines
        test_array[4] = self.Conductivity
        test_array[5] = self.Organic_carbon
        test_array[6] = self.Trihalomethanes
        test_array[7] = self.Turbidity
        print(test_array)

        predict = self.model.predict([test_array])[0]
      
        return predict

        