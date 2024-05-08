import pandas as pd
import numpy as np

# Define the number of data points
num_data_points = 100

# Generate random data for the columns
data = {
    'avg_temp_i': np.round(np.random.uniform(18, 28, num_data_points), 3),  # Random values for interior temperature (degrees Celsius)
    
    'avg_temp_e': np.round(np.random.uniform(10, 30, num_data_points), 3),  # Random values for exterior temperature (degrees Celsius)
    
    'avg_hum_i': np.round(np.random.uniform(40, 80, num_data_points), 3),   # Random values for interior humidity (%)
    
    'avg_hum_e': np.round(np.random.uniform(30, 90, num_data_points), 3),   # Random values for exterior humidity (%)
    
    'med_c': np.random.choice(['Sustrato'], num_data_points),  # Random selection of cultivation medium
    # Medios ['Sustrato', 'Living Soil', 'Hydroponia']
    
    'gen': np.random.choice(['Gorilla Glue', '24/7'], num_data_points, p=[0.5, 0.5]),  # Random selection of genetics
    
    'location': np.random.randint(1, 21, num_data_points),  # Random location ID (1-20)
    
    'grower_id': np.random.randint(1, 21, num_data_points),  # Random grower ID (1-20)
    
    'grower_name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Emma'], num_data_points),  # Random grower name
    
    'grower_xp': np.random.randint(1, 11, num_data_points),  # Random grower experience (years)

    'avg_GxP': np.zeros(num_data_points),  # Placeholder for grams per plant, to be filled later

}

# Create DataFrame
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
