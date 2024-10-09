import pandas as pd

file_path = 'updated_file.csv' 
df = pd.read_csv(file_path)

ocean_coordinates = {
    'SouthEast Atlantic Ocean': {'latitude': -25.0, 'longitude': 0.0},
    'SouthWest Atlantic Ocean': {'latitude': -35.0, 'longitude': -50.0},
    'NorthWest Atlantic Ocean': {'latitude': 35.0, 'longitude': -75.0},
    'NorthEast Atlantic Ocean': {'latitude': 45.0, 'longitude': -10.0},
    'Central Atlantic Ocean': {'latitude': 0.0, 'longitude': -30.0},
    'SouthWest Pacific Ocean': {'latitude': -35.0, 'longitude': 160.0},
    'SouthEast Pacific Ocean': {'latitude': -30.0, 'longitude': -110.0},
    'NorthWest Pacific Ocean': {'latitude': 35.0, 'longitude': 140.0},
    'NorthEast Pacific Ocean': {'latitude': 25.0, 'longitude': -130.0},
    'Central Pacific Ocean': {'latitude': 0.0, 'longitude': -160.0},
    'North Indian Ocean': {'latitude': 10.0, 'longitude': 80.0},
    'South Indian Ocean': {'latitude': -30.0, 'longitude': 90.0},
    'Arabian Gulf': {'latitude': 25.0, 'longitude': 55.0},
    'North Red Sea': {'latitude': 25.0, 'longitude': 35.0},
    'South Red Sea': {'latitude': 15.0, 'longitude': 40.0}
}

# Function to assign ocean coordinate based on the country
def assign_ocean_coordinate(country):
    if country in ['Brazil', 'Argentina', 'Uruguay', 'Bermuda']:
        return 'SouthWest Atlantic Ocean'
    elif country in ['South Africa', 'Namibia', 'Angola']:
        return 'SouthEast Atlantic Ocean'
    elif country in ['United States', 'Canada']:
        return 'NorthWest Atlantic Ocean'
    elif country in ['United Kingdom', 'Portugal', 'Spain','Ireland','France']:
        return 'NorthEast Atlantic Ocean'
    elif country in ['Cuba', 'Belize', 'Mexico', 'Trinidad and Tobago','Bahamas','Cayman Islands',
      'Turks and Caicos','Jamaica','Honduras','Haiti','Ivory Coast','Barbados','Martinique','Antigua and Barbuda',
      'Saint Lucia', 'Saint Vincent and the Grenadines','Grenada','Montserrat','Saint Kitts and Nevis','Morocco',
      'Dominican Republic','Puerto Rico','Bermuda','Senegal', 'Guatemala']:
        return 'Central Atlantic Ocean'
    elif country in ['French Polynesia','Australia','New Zealand','Papua New Guinea','Solomon Islands',
   'Fiji', 'Vanuatu','New Caledonia']:
        return 'SouthWest Pacific Ocean'
    elif country in ['New Zealand','Ecuador','Peru','Panama','Costa Rica','Nicaragua']:
        return 'SouthEast Pacific Ocean'
    elif country in ['Japan', 'China','Taiwan','South Korea','Philippines','Malaysia','Vietnam',
'Thailand','Brunei','Cambodia']:
        return 'NorthWest Pacific Ocean'
    elif country in ['United States', 'Canada']:
        return 'NorthEast Pacific Ocean'
    elif country in ['Colombia', 'Kiribati','Marshall Islands','Palau','Tuvalu','Cook Islands',
      'Tonga','Samoa']:
        return 'Central Pacific Ocean'
    elif country in ['India','Sri Lanka','Maldives','Bangladesh']:
        return 'North Indian Ocean'
    elif country in ['Seychelles','Mauritius','Madagascar','Comoro Islands','Tanzania','Mozambique']:
        return 'South Indian Ocean'
    elif country in ['Saudi Arabia', 'United Arab Emirates','Bahrain','Oman','Kuwait','Iran']:
        return 'Arabian Gulf'
    elif country in ['Egypt', 'Jordan', 'Israel','Sudan']:
        return 'North Red Sea'
    elif country in ['Yemen', 'Eritrea','Djibouti']:
        return 'South Red Sea'
    else:
        return None

# Apply the ocean coordinate function and add latitude and longitude
df['ocean_coordinate'] = df['Country'].apply(assign_ocean_coordinate)

df['latitude'] = df['ocean_coordinate'].map(lambda ocean: ocean_coordinates.get(ocean, {}).get('latitude'))
df['longitude'] = df['ocean_coordinate'].map(lambda ocean: ocean_coordinates.get(ocean, {}).get('longitude'))

#Save the updated DataFrame to a new CSV
df.to_csv('correct_file.csv', index=False)

# for ocean in ocean_coordinates:
#     ocean_df = df[df['ocean_coordinate'] == ocean]
#     file_name = f'{ocean.replace(" ", "_").lower()}.csv'
#     ocean_df.to_csv(file_name, index=False)
#     print(f'Saved {file_name}')
