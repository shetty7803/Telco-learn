import requests
import logging

logging.basicConfig(
    filename="api_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_api_call(func):
    def wrapper(url):
        print(f"[Decorator] Calling API: {url}")
        logging.info(f"API call started: {url}")
        return func(url)
    return wrapper

@log_api_call
def fetch_data(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status() 
        return response.json()

    except requests.exceptions.Timeout:
        print("Timeout error!")
        logging.error("Timeout error")
        return None

    except requests.exceptions.ConnectionError:
        print("Connection error!")
        logging.error("Connection error")
        return None

    except requests.exceptions.HTTPError:
        print("HTTP error!")
        logging.error("HTTP error")
        return None

    except Exception as e:
        print(f"Unknown error: {e}")
        logging.error(f"Unknown error: {e}")
        return None


print("GOOD URL")
print(fetch_data("https://api.restful-api.dev/objects"))

print("BAD URL")
print(fetch_data("https://jsonplaceholder.typicode.com/todos_wrong"))

