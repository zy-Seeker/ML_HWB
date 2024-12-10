import xarray as xr
import numpy as np
import os
from datetime import datetime, timedelta

# Function to read and extract the relevant slices from each file
def read_and_slice(file_path):
    with xr.open_dataset(file_path) as ds:
        return ds.variables['u10' if 'u_component' in file_path else 'v10'][0].values

# Define the base path where the data is stored
base_path = '/home/ml_2024/students/07_zengyi/target_data'  # Modify this path according to where the data is stored


# Define your start date
start_date = datetime(2018, 9, 9)  # Modify this according to your start date

# Loop over 7 days
for i in range(8):
    # Calculate the current date
    current_date = start_date + timedelta(days=i)

    # Format the year, month, and date in the desired format
    date_str = current_date.strftime('%Y-%m-%d')

    # Define the file paths for u10 and v10
    u10_file_path = os.path.join(base_path, date_str, '10m_u_component_of_wind', 'surface.nc')
    v10_file_path = os.path.join(base_path, date_str, '10m_v_component_of_wind', 'surface.nc')

    # Read and slice the data for u10 and v10
    u10_data = read_and_slice(u10_file_path)
    v10_data = read_and_slice(v10_file_path)

    # Construct the filename for the numpy array
    npy_filename = os.path.join(base_path,date_str, f'surface_wind_{date_str}.npy')

    # Stack u10 and v10 into a single array and save it
    stacked_data = np.stack((u10_data, v10_data))
    np.save(npy_filename, stacked_data)