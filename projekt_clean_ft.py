import os
import pandas as pd

#SRC = os.path.join( "temps.csv")

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def clean_data(file_path, usecols, column_names):
    pdcfg = {
    'usecols' : usecols,
    'thousands' : ' ',
    'skiprows' : 1,
    'header' : None,
    'na_values' : ['nd'],
    'parse_dates' : ['Date'],
    'names' : column_names,
    }
    projekt = pd.read_csv(file_path, **pdcfg)

    if 'Date' in projekt.columns:
        projekt['Date'] = pd.to_datetime(projekt['Date'], errors='coerce')
        projekt['Year_Month'] = projekt['Date'].dt.to_period('M').astype(str)
        projekt.drop(columns=['Date'], inplace=True)

    if 'Temperature_Mean' in projekt:
        projekt['Temperature_Mean'] = projekt['Temperature_Mean'].apply(kelvin_to_celsius)
    if 'Temperature_MIN' in projekt:
        projekt['Temperature_MIN'] = projekt['Temperature_MIN'].apply(kelvin_to_celsius)
    if 'Temperature_Mean' in projekt:
        projekt['Temperature_MAX'] = projekt['Temperature_MAX'].apply(kelvin_to_celsius)

    #print("Missing Values:")
    #print(projekt.isna().sum())

    projekt['Row_Min'] = projekt[['Temperature_Mean', 'Temperature_MIN', 'Temperature_MAX']].min(axis=1)
    projekt['Row_Max'] = projekt[['Temperature_Mean', 'Temperature_MIN', 'Temperature_MAX']].max(axis=1)
    for index, row in projekt.iterrows():
        for column in ['Temperature_Mean', 'Temperature_MIN', 'Temperature_MAX']:
            if pd.isna(row[column]):
                projekt.at[index, column] = (row['Row_Min'] + row['Row_Max']) / 2
    projekt = projekt.drop(columns=['Row_Min', 'Row_Max'])

    #print(projekt.isna().sum())
    #projekt_cleaned = projekt.dropna()

    #print("\nDuplicate Rows:")
    #print(projekt.duplicated().sum())
    projekt.drop_duplicates(inplace=True)
    projekt.dropna(subset=['Temperature_Mean', 'Temperature_MAX', 'Percent_Bleaching'], inplace=True)
    #print(projekt.duplicated().sum())

    #print("\nData Types:")
    #print(projekt.dtypes)

#if __name__ == "__main__":
    # script byl volan primo 
  #  clean_data()
    return (projekt)

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, './temps.csv')
usecols = [5, 9, 20, 24, 27, 28, 29, 58]
column_names = ['Ocean', 'Country', 'Depth_M', 'Percent_Bleaching', 'Temperature_Mean','Temperature_MIN','Temperature_MAX','Date']

clean_data(file_path, usecols, column_names)
print("Data cleaned.")