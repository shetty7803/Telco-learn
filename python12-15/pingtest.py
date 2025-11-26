import subprocess
import os
import logging

logging.basicConfig(filename='log.txt', level=logging.WARNING)
logging.debug('debug information')
logging.info('info information')
logging.warning('warning information')
logging.error('error information')
logging.critical('critical information')
ip_list = ["192.168.1.13", "8.8.8.8", "1.1.1.1", "127.0.0.1", "127.0.0.2", "192.168.1.12"]

for ip in ip_list:
    try:
        result = subprocess.run(
            ["ping", "-c", "1", ip],
            capture_output=True,
            text=True,
            timeout=2
        )

        print(result.stdout)

        if result.returncode == 0:
            print(f"{ip} works.\n")
        else:
            print(f"{ip} fails.\n")

    except subprocess.TimeoutExpired:
        print(f"Timeout: {ip} did not respond in time.\n")

    except FileNotFoundError:
        print("Error: 'ping' command not found on this system.\n")
        break

    except Exception as e:
        print(f"Unexpected error on {ip}: {e}\n")
