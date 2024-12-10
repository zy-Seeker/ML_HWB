import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import os
import pandas as pd

# Custom extent (min_lon, min_lat, max_lon, max_lat)
custom_extent = (110, 160, 5, 35)  # Correct extent for the Caribbean region

# Create a meshgrid of longitudes and latitudes
lon = np.linspace(0.125, 359.875, 1440)
lat = np.linspace(90, -90, 721)
lon_grid, lat_grid = np.meshgrid(lon, lat)

# Define the base path where the data is stored
base_path = '/home/ml_2024/students/07_zengyi/target_data'

# Define the start and end dates
start_date = '2018-09-09'
end_date = '2018-09-16'

# Generate the list of dates between start and end dates
dates = [d.strftime('%Y-%m-%d') for d in pd.date_range(start_date, end_date)]

# Create a figure and subplots
fig, axes = plt.subplots(1, len(dates), figsize=(20, 4), subplot_kw={'projection': ccrs.PlateCarree()})

# Create levels for the contour ranging from 0 to 80 m/s
levels = np.linspace(0, 40, num=10)  # This creates 10 levels from 0 to 40 inclusive

# Loop over the dates and axes
for date, ax in zip(dates, axes):
    # Construct the file path for the current date
    file_path = os.path.join(base_path, date, f'surface_wind_{date}.npy')

    # Load the data from the file
    temp = np.load(file_path)
    u10 = temp[0, :, :]
    v10 = temp[1, :, :]

    # Calculate wind speed from u10 and v10
    wind_speed = np.sqrt(u10**2 + v10**2)

    # Set the extent of the map to the custom region
    ax.set_extent(custom_extent, crs=ccrs.PlateCarree())

    # Plot the wind speed map with specified levels
    c = ax.contourf(lon_grid, lat_grid, wind_speed, levels=levels, cmap='viridis', extend='both', transform=ccrs.PlateCarree())

    # Add coastlines and borders
    ax.coastlines(resolution='110m', color='black', linewidth=0.8)
    ax.add_feature(cfeature.BORDERS, linestyle='-', edgecolor='black', linewidth=0.5)

    # Set the subplot title
    ax.set_title(date, fontsize=12)

# Remove the space between subplots
plt.subplots_adjust(wspace=0)

# Display the plot
plt.show()