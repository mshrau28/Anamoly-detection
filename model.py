import pandas as pd
import numpy as np
import keras
import pickle
import scipy.stats
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier


def transform_data(dataset):
 feature_dataset = {'Measured_RPM':[],'Kurtosis_1':[],'std_1':[],'Kurtosis_2':[],'std_2':[],'Kurtosis_3':[],'std_3':[]}
 RPMs = list(dataset.Measured_RPM.unique())

 for RPM in RPMs:
   RPM_data = dataset[dataset.Measured_RPM == RPM]
   RPM_data.reset_index(inplace = True)
   samples = int(RPM_data.shape[0]/4096)
 
   for i in range(samples):
     feature_dataset['Measured_RPM'].append(RPM)
     feature_dataset['Kurtosis_1'].append(RPM_data[0+i*4096:4096+i*4096].Vibration_1.kurtosis())
     feature_dataset['std_1'].append(RPM_data[0+i*4096:4096+i*4096].Vibration_1.std())

     feature_dataset['Kurtosis_2'].append(RPM_data[0+i*4096:4096+i*4096].Vibration_2.kurtosis())
     feature_dataset['std_2'].append(RPM_data[0+i*4096:4096+i*4096].Vibration_2.std())

     feature_dataset['Kurtosis_3'].append(RPM_data[0+i*4096:4096+i*4096].Vibration_3.kurtosis())
     feature_dataset['std_3'].append(RPM_data[0+i*4096:4096+i*4096].Vibration_3.std())
 
 X = pd.DataFrame(feature_dataset).to_numpy()
 
 return X


def show_output(vibration_data_path,text_label):    #displays output
    
    #loading the model
    model = pickle.load(open("RF_Trained_Model",'rb'))
    output = {1:"Normal Data",0:"Unbalance detected"}

    input_data = pd.read_csv(vibration_data_path)
    modified_data = transform_data(input_data)
    modified_data = modified_data[0].reshape(1,7)
   
    text_label.config(text = output[model.predict(modified_data)[0]])
     
     

    
    

