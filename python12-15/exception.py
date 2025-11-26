import requests  

class InvalidAPIResponse(Exception):
    pass


def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url, timeout=5) 
        
        response.raise_for_status()  

        try:
            data = response.json() 
        except ValueError:
            raise InvalidAPIResponse("Response is not valid JSON")

        print("Data fetched successfully!")
        return data

    except requests.exceptions.Timeout:
        print("Error: Request timed out!")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed!")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except InvalidAPIResponse as e:
        print(f"Custom Error: {e}")
    except Exception as e:
        print(f"Unexpected Error: {e}")


good_url = "https://api.restful-api.dev/objects"
print(fetch_data(good_url))

bad_url = "https://jsonplaceholder.typicode.com/todos_wrong"
print(fetch_data(bad_url))

bad_json_url = "https://example.com"
print(fetch_data(bad_json_url))

