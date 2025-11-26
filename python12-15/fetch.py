import requests   # required module
import logging

logging.basicConfig(filename='log1.txt', level=logging.WARNING)
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')

# Function to fetch data from API
def fetch_data(url):
    try:
        print(f"Fetching data from: {url}")
        response = requests.get(url, timeout=5)   # send request
        
        response.raise_for_status()  # raise exception for 4xx/5xx errors
        
        data = response.json()       # convert response to JSON
        print("Data fetched successfully!")
        return data

    except requests.exceptions.Timeout:
        print("Error: Request timed out!")
    except requests.exceptions.ConnectionError:
        print("Error: Connection failed!")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP Error: {http_err}")
    except Exception as e:
        print(f"Unexpected Error: {e}")

# ------------------------
# TESTING WITH GOOD URL
good_url = "https://api.restful-api.dev/objects"
print(fetch_data(good_url))

# TESTING WITH BAD URL
bad_url = "https://jsonplaceholder.typicode.com/todos_wrong"
print(fetch_data(bad_url))
