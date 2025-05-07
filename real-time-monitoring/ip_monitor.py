import time
import requests
import psutil
import json

def get_current_ip():
    try:
        response = requests.get("https://api.ipify.org?format=json")
        return response.json()['ip']
    except Exception as e:
        print(f"Error getting IP address: {e}")
        return None

def monitor_ip_changes():
    last_ip = None
    while True:
        current_ip = get_current_ip()
        if current_ip != last_ip:
            print(f"IP address changed! New IP: {current_ip}")
            last_ip = current_ip
        time.sleep(60)  # Check every minute
