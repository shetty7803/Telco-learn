import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

headers = {
    "Authorization": "Bearer TOKEN_VALUE",
    "Content-Type": "application/json"
}

# ---------- GET ----------
response = requests.get(url, headers=headers)
data = response.json()

with open("get_token_output.json", "w") as f:
    json.dump(data, f)

# ---------- POST ----------
payload = {"key": "value"}
response = requests.post(url, json=payload, headers=headers)
data = response.json()

with open("post_token_output.json", "w") as f:
    json.dump(data, f)

# ---------- PUT ----------
payload = {"key": "updated_value"}
response = requests.put(url, json=payload, headers=headers)
data = response.json()

with open("put_token_output.json", "w") as f:
    json.dump(data, f)

# ---------- PATCH ----------
payload = {"key": "partial_update"}
response = requests.patch(url, json=payload, headers=headers)
data = response.json()

with open("patch_token_output.json", "w") as f:
    json.dump(data, f)

# ---------- DELETE ----------
response = requests.delete(url, headers=headers)

with open("delete_token_output.txt", "w") as f:
    f.write(str(response.status_code))
    json.dump(data, f, indent=4)