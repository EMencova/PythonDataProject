import os
import pandas as pd
from Muj_projekt.projekt_clean_ft import clean_data

projekt_data = clean_data()

def split_oceans_to_csv(df, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    grouped = df.groupby('Ocean')

    for ocean, data in grouped:
        ocean_filename = f"{ocean.replace(' ', '_').lower()}_data.csv"
        output_path = os.path.join(output_dir, ocean_filename)
        data.to_csv(output_path, index=False)
        print(f"Saved {ocean} data to {output_path}")
        
split_oceans_to_csv(projekt_data, 'Atlantik')