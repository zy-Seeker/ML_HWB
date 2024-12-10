import os

# Define your variables
year = '2018'  # e.g., '2020'
month = '09'   # e.g., '01' for January; ensure it's a two-digit format
date = '27'    # e.g., '15'; also ensure it's two-digit format

# Construct the command string using Python's f-string for formatting
command = f"gsutil -m cp -r " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-pressure_level/{year}/{month}/{date}/geopotential " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-pressure_level/{year}/{month}/{date}/specific_humidity " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-pressure_level/{year}/{month}/{date}/temperature " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-pressure_level/{year}/{month}/{date}/u_component_of_wind " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-pressure_level/{year}/{month}/{date}/v_component_of_wind " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-single_level/{year}/{month}/{date}/mean_sea_level_pressure " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-single_level/{year}/{month}/{date}/10m_u_component_of_wind " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-single_level/{year}/{month}/{date}/10m_v_component_of_wind " \
          f"gs://gcp-public-data-arco-era5/raw/date-variable-single_level/{year}/{month}/{date}/2m_temperature " \
          f"."

# Run the command
os.system(command)