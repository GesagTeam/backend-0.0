import requests
import pandas as pd
from boxsdk import OAuth2, Client

# Fetch University Data and Save as Excel (simplified for clarity)
country = "Germany"
url = f"http://universities.hipolabs.com/search?country={country}"
response = requests.get(url)

if response.status_code == 200:
    universities_data = response.json()
    all_universities_info = []
    for university in universities_data:
        uni_info = {
            "Name": university.get('name', 'N/A'),
            "Country": university.get('country', 'N/A'),
            "State/Province": university.get('state-province', 'N/A'),
            "Alpha Two Code": university.get('alpha_two_code', 'N/A'),
            "Domains": ", ".join(university.get('domains', [])),
            "Web Pages": ", ".join(university.get('web_pages', []))
        }
        all_universities_info.append(uni_info)

    df = pd.DataFrame(all_universities_info)
    df_sorted = df.sort_values(by='Name', ascending=True)
    excel_filename = f"{country}_universities_sorted.xlsx"
    df_sorted.to_excel(excel_filename, index=False)
    print(f"Data has been successfully sorted and saved to {excel_filename}")

    # Box API setup
    oauth = OAuth2(
        client_id='vb1lc5vmxmdkow5q5phzwcude3c5xqcq',  # Replace with your Box client ID
        client_secret='PpskEkoFshHCQRGfsYQcX1nAIz3o0Hab',  # Replace with your Box client secret
        access_token='RvP19yGx5KwIzh23V7e2y3Zka4A9fujN'  # Replace with your Box access token
    )
    client = Client(oauth)

    # Upload the file to Box
    with open(excel_filename, 'rb') as file:
        root_folder = client.folder('0')  # '0' is the root folder ID in Box
        root_folder.upload_stream(file, excel_filename)

    print(f"File has been uploaded to Box with the title: {excel_filename}")

else:
    print(f"Failed to retrieve data: {response.status_code}")
