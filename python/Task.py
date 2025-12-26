# import requests
# import json 

# url1 = "https://api.open-meteo.com/v1/forecast?latitude=12.9719&longitude=77.5937&hourly=temperature_2m"
# url2 = "https://api.open-meteo.com/v1/forecast?latitude=40.7143&longitude=-74.006&hourly=temperature_2m"

# response1 = requests.get(url1)
# response2 = requests.get(url2)
# combined = [response1.json(), response2.json()]

# with open('weather_data.json', 'w') as file:
#     json.dump(combined, file, indent=4)

#--------------------------------------------------------------------------

import requests

url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
print("response status:", response.status_code)


if response.status_code == 200:
     print(response.json())
else:
     print("Error parsing JSON")

