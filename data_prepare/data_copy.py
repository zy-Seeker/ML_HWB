from datetime import datetime, timedelta
import os

# Define your start date
start_year = 2018
start_month = 9
start_day = 9

# Create a datetime object for the start date
start_date = datetime(start_year, start_month, start_day)

# Loop over 7 days
for i in range(8):
    # Calculate the current date
    current_date = start_date + timedelta(days=i)

    # Format the year, month, and date in two-digit format
    year = current_date.strftime('%Y')
    month = current_date.strftime('%m')
    date = current_date.strftime('%d')

    # Create the folder for the current date if it doesn't exist
    folder_path = f"./{year}-{month}-{date}/"
    os.makedirs(folder_path, exist_ok=True)

    # Construct the command string using Python's f-string for formatting
    command = (f"gsutil -m cp -r "
               f"gs://gcp-public-data-arco-era5/raw/date-variable-single_level/{year}/{month}/{date}/10m_u_component_of_wind "
               f"gs://gcp-public-data-arco-era5/raw/date-variable-single_level/{year}/{month}/{date}/10m_v_component_of_wind "
               f"{folder_path}")

    # Execute the command using !{command} in Colab
    print(f"Downloading data for {year}-{month}-{date}...")
    os.system(command)