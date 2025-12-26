# import requests

# TOKEN = "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"
# headers = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Accept": "application/vnd.github+json"
# }

# url = "https://api.github.com/users/DevJarvis11"
# responses = requests.get(url, headers=headers)

# print("Status Code:", responses.status_code)
# print("Response:", responses.json()) 

# import requests
# import json

# # Your existing credentials and headers
# TOKEN = "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"
# headers = {
#     "Authorization": f"Bearer {TOKEN}",
#     "Accept": "application/vnd.github+json"
# }

# url = "https://api.github.com/users/DevJarvis11"
# responses = requests.get(url, headers=headers)

# # Check if the request was successful
# if responses.status_code == 200:
#     data = responses.json()
    
#     # Save to a JSON file
#     with open('github_user_response.json', 'w', encoding='utf-8') as f:
#         json.dump(data, f, indent=4)
    
#     print("Status Code:", responses.status_code)
#     print("Success! Response saved to 'github_user_response.json'")
# else:
#     print(f"Error: {responses.status_code}")
#     print(responses.text)


#-----------------------------------------------------------------------------

import requests
import json

# 1. Configuration
# No token required for this public test API
URL = "https://jsonplaceholder.typicode.com/users/1"

# 2. Execution - Get the data
response = requests.get(URL)

if response.status_code == 200:
    # Convert response to a Python Dictionary
    data = response.json()

    # 3. Save the full response to a JSON file
    with open('user_data.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
    print("Full response saved to 'user_data.json'")

    # 4. Fetch parameters from nested dictionaries
    # Level 1: address (Dictionary)
    # Level 2: geo (Dictionary inside address)
    # Level 3: lat (Value inside geo)
    
    city = data.get("address", {}).get("city")
    latitude = data.get("address", {}).get("geo", {}).get("lat")

    print("-" * 30)
    print(f"City (Level 1 nested): {city}")
    print(f"Latitude (Level 2 nested): {latitude}")
    print("-" * 30)

else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
