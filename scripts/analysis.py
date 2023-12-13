import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv("data/cardata.csv")

# Convert 'persons' to a numeric type, coercing non-numeric values to NaN
df['persons'] = pd.to_numeric(df['persons'], errors='coerce')


## Buying price frequency bar graph
plt.figure(figsize=(8, 6))
sns.countplot(x='buying', data=df)
plt.title('Frequency Distribution of Buying Cars')
plt.savefig('results/buying.png')
plt.show()



