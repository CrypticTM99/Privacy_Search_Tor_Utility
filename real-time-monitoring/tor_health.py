import time
import requests

def check_tor_connection():
    try:
        response = requests.get("https://check.torproject.org/api/ip")
        if response.status_code == 200:
            data = response.json()
            if data.get("Tor", False):
                print("Tor connection is active.")
                return True
            else:
                print("Tor is not active.")
                return False
    except Exception as e:
        print(f"Error checking Tor connection: {e}")
        return False

def monitor_tor_connection():
    while True:
        tor_status = check_tor_connection()
        if not tor_status:
            print("Warning: Tor connection lost!")
        time.sleep(60)  # Check every minute
