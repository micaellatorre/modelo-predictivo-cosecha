import pandas as pd
import numpy as np
from datetime import datetime, timedelta
# Load VPD chart values from CSV file
# vpd_chart = pd.read_csv('vpd_chart.csv')

# Interpolate VPD values based on temperature and humidity measurements
# def calculate_vpd(temp_i, hum_i):
#     # Interpolate VPD value from the VPD chart
#     vpd_value = np.interp(temp_i, vpd_chart['Temperature'], vpd_chart['Humidity'])
#     return vpd_value

# Define the number of measurements per day and the duration of the experiment
num_measurements_per_day = 6  # 6 measurements per day
num_days = 90  # Approximately 3 months

# Get data from Grower Form

# Generate constant values for the grower
grower_data = {
    'grower_id': 1,  # Assuming the grower ID
    'grower_name': 'Carlos Sosa M',  # Assuming the grower's name
    'grower_xp': 5,  # Assuming the grower's experience
    'location': np.random.choice(['Uruguay'], 1)[0],  # Controlled location
    'med_c': np.random.choice(['Sustrato'], 1)[0],  # Controlled cultivation medium
    'gen': np.random.choice(['Gorilla Glue', '24/7'], p=[0.5, 0.5])  # Controlled genetics
}

# Create DataFrame with grower values
grower_df = pd.DataFrame(grower_data, index=[0])

# Generate time indices for each measurement
start_date = datetime(2024, 3, 17, 9, 0)  # Start at 9:00 am
time_indices = [start_date + timedelta(hours=3 * i) for i in range(num_days * num_measurements_per_day)]

# Generate measurements for the grower
measurements_data = {
    'time': time_indices,
    # 'grower_id': np.full(num_days * num_measurements_per_day, grower_df['grower_id'].iloc[0]),
    # 'grower_name': np.full(num_days * num_measurements_per_day, grower_df['grower_name'].iloc[0]),
    # 'grower_xp': np.full(num_days * num_measurements_per_day, grower_df['grower_xp'].iloc[0]),
    # 'gen': np.full(num_days * num_measurements_per_day, grower_df['gen'].iloc[0]),
    # 'med_c': np.full(num_days * num_measurements_per_day, grower_df['med_c'].iloc[0]),
    
    'temp_i': np.round(np.random.uniform(18, 28, num_days * num_measurements_per_day), 1),
    'hum_i': np.round(np.random.uniform(40, 80, num_days * num_measurements_per_day), 1),
    'temp_e': np.round(np.random.uniform(10, 30, num_days * num_measurements_per_day), 1),
    'hum_e': np.round(np.random.uniform(30, 90, num_days * num_measurements_per_day), 1),
    # 'lux_i': averiguar rango, VER CURSO
    
    # Add a colum for the Vapor Preasure Deficit calculation accessing a csv file with the VPD chart values. This chart has temperature in one index and humidity in the other index. Take in mind this calculation is made from the inside measurements, this being temp_i and hum_i
    
    # 'vpd': [calculate_vpd(temp_i, hum_i) for temp_i, hum_i in zip(np.round(np.random.uniform(18, 28, num_days * num_measurements_per_day), 1), 
    #                                                               np.round(np.random.uniform(40, 80, num_days * num_measurements_per_day), 1))]
}

# Create DataFrame for measurements
measurement_df = pd.DataFrame(measurements_data)

# Display the first 10 rows of the DataFrame
print(measurement_df)
