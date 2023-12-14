import pandas as pd
import os

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