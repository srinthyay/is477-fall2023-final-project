from ydata_profiling import ProfileReport
import pandas as pd
import os 


# Assign the column names to the DataFrame
df = pd.read_csv('data/cardata.csv')

if not os.path.exists("profiling"):
    os.makedirs("profiling")

profile = ProfileReport(df, title="Profiling Report")
profile.to_file("profiling/profiling.html")       