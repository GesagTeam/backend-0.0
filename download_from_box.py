import requests
import pandas as pd
from boxsdk import OAuth2, Client
import os

# Box API setup
oauth = OAuth2(
    client_id='vb1lc5vmxmdkow5q5phzwcude3c5xqcq',
    client_secret='PpskEkoFshHCQRGfsYQcX1nAIz3o0Hab',
    access_token='RvP19yGx5KwIzh23V7e2y3Zka4A9fujN'
)
client = Client(oauth)

# Step 1: Download the file from Box
file_name = "Germany_universities_sorted.xlsx"
download_folder = "."  # Specify the folder where you want to save the file

# Search for the file in Box
items = client.search().query(query=file_name, limit=100, offset=0, ancestor_folders=[client.folder('0')])

# Iterate over the search results
file_found = False
for item in items:
    if item.name == file_name:
        file_found = True
        file_path = os.path.join(download_folder, file_name)
        with open(file_path, 'wb') as f:
            item.download_to(f)
        print(f"File downloaded successfully to {file_path}")
        break

if not file_found:
    print(f"File {file_name} not found in Box.")

# Step 2: Read the downloaded Excel file
if file_found:
    df = pd.read_excel(file_path)

    # Step 3: Print the university names
    university_names = df['Name'].tolist()
    print("University Names:")
    for name in university_names:
        print(name)
