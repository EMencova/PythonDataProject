import pandas as pd
import os

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, './oceans','sorted_atlantic_data.csv')

atlantik = pd.read_csv(file_path)
atlantik['index'] = range(1, len(atlantik) + 1)
atlantik.insert(0, 'index', atlantik.pop('index'))
print("before dropping mean temp")
atlantik.info()
print("after dropping mean temp")

#for index, row in atlantik in atlantik.iterrows():
 #   if pd.isnull(row['Temperature_Mean']):

atlantik.dropna(subset=['Temperature_Mean', 'Temperature_MAX', 'Percent_Bleaching'], inplace=True)
atlantik.info()

        
