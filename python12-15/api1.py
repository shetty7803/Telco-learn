import requests, json

respone = requests.get("http://www.3gpp.org/ftp/Specs/archive/24_series/24.283/")
data = respone.json()

print(data)