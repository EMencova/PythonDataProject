import os
import pandas as pd

#ArabSRC = './oceans/arabian_ocean_data.csv'
#Arabian = pd.read_csv(ArabSRC)
#Arabian.info()

import pandas as pd
import os

def process_sep_files(file_name, output_dir):

  
    script_dir = os.path.dirname(__file__)
    file_path = os.path.join(script_dir,'oceans', file_name)
    pdcfg = {
        'na_values': ['nd'],
        'parse_dates': [7]
        }

    file = pd.read_csv(file_path, **pdcfg)
    file['Year_Month'] = file['Year_Month'].dt.to_period('M').astype(str)
    sorted_file = file.sort_values(['Year_Month'],ascending=[True])
    output_path = os.path.join(script_dir, output_dir, f'sorted_{file_name}')
    sorted_file.dropna(subset=['Temperature_Mean', 'Temperature_MAX', 'Percent_Bleaching'], inplace=True)
    #atlantik['index'] = range(1, len(atlantik) + 1)
   # atlantik.insert(0, 'index', atlantik.pop('index'))
    sorted_file.to_csv(output_path, index=False)
    print("Sorted Data saved in Oceans folder")
    return sorted_file

process_sep_files('pacific_data.csv', 'oceans')
