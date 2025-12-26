import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

# ---------- GET ----------
response = requests.get(url)
data = response.json()

# Write GET response to file
with open("get_output.json", "w") as f:
    json.dump(data, f)

# ---------- POST ----------
payload = {"key": "value"}
response = requests.post(url, json=payload)
data = response.json()

with open("post_output.json", "w") as f:
    json.dump(data, f)

# ---------- PUT ----------
payload = {"key": "updated_value"}
response = requests.put(url, json=payload)
data = response.json()

with open("put_output.json", "w") as f:
    json.dump(data, f)

# ---------- PATCH ----------
payload = {"key": "partial_update"}
response = requests.patch(url, json=payload)
data = response.json()

with open("patch_output.json", "w") as f:
    json.dump(data, f)

# ---------- DELETE ----------
response = requests.delete(url)

# Write delete status to file
with open("delete_output.txt", "w") as f:
    f.write(str(response.status_code))
