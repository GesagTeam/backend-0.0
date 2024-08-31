import requests
import pandas as pd
import os

# API Endpoint
country = "Germany"  # You can change this to any country you're interested in
url = f"http://universities.hipolabs.com/search?country={country}"

# Send a GET request to the API
response = requests.get(url)

if response.status_code == 200:
    universities_data = response.json()

    # List to hold all the university information
    all_universities_info = []

    # Process each university's data
    for university in universities_data:
        uni_info = {
            "Name": university.get('name', 'N/A'),
            "Country": university.get('country', 'N/A'),
            "State/Province": university.get('state-province', 'N/A'),
            "Alpha Two Code": university.get('alpha_two_code', 'N/A'),
            "Domains": ", ".join(university.get('domains', [])),
            "Web Pages": ", ".join(university.get('web_pages', []))
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
    excel_filename = os.path.join(downloads_path, f"{country}_universities_sorted.xlsx")
    df_sorted.to_excel(excel_filename, index=False)

    print(f"Data has been successfully sorted and saved to {excel_filename}")

else:
    print(f"Failed to retrieve data: {response.status_code}")
