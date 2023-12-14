import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import numpy as np

car_data = pd.read_csv("data/cardata.csv")
output_dir = 'results/'
os.makedirs(output_dir, exist_ok=True)

for col in car_data.columns:
   if car_data[col].dtype == 'object':
       print(f'{col}:')
       print(car_data[col].value_counts())

for col in car_data.columns:
   if car_data[col].dtype == 'object':
       print(f'{col}:')
       print(car_data[col].value_counts(normalize=True)) 

summary_stats = car_data.describe()
summary_stats.to_csv(os.path.join(output_dir, 'summary_stats.csv'))



