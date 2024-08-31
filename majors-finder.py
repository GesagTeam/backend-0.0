import requests
import pandas as pd
import os

# Hypothetical API endpoint for StudyPortals
base_url = "https://api.studyportals.com/v1/universities"
country = "Germany"

# API parameters
params = {
    "country": country,
    # Additional parameters could include filtering by program type, language, etc.
}

# Hypothetical API Key (You would get this after subscribing or partnering with StudyPortals)
api_key = "your_api_key_here"

# Headers for the API request
headers = {
    "Authorization": f"Bearer {api_key}",
    "Accept": "application/json",
}

# Send a GET request to the StudyPortals API
response = requests.get(base_url, params=params, headers=headers)

if response.status_code == 200:
    universities_data = response.json()

    # List to hold all the university information
    all_universities_info = []

    # Process each university's data
    for university in universities_data['data']:
        uni_info = {
            "Name": university.get('name', 'N/A'),
            "Country": university.get('country', 'N/A'),
            "City": university.get('city', 'N/A'),
            "Programs": ", ".join([program['name'] for program in university.get('programs', [])]),
            "Tuition Fees": university.get('tuition_fees', 'N/A'),
            "Language": university.get('language', 'N/A'),
            "Duration": university.get('duration', 'N/A'),
            "Web Pages": university.get('website', 'N/A'),
        }

        # Append the dictionary to the list
        all_universities_info.append(uni_info)

    # Create a DataFrame from the collected data
    df = pd.DataFrame(all_universities_info)

    # Sort the DataFrame by the 'Name' column alphabetically
    df_sorted = df.sort_values(by='Name', ascending=True)

    # Get the path to the user's Downloads folder
    downloads_path = os.path.join(os.path.expanduser("~"), "Downloads")

    # Save the sorted DataFrame to an Excel file in the Downloads folder
    excel_filename = os.path.join(downloads_path, f"{country}_universities_studyportals.xlsx")
    df_sorted.to_excel(excel_filename, index=False)

    print(f"Data has been successfully retrieved and saved to {excel_filename}")

else:
    print(f"Failed to retrieve data: {response.status_code}")
