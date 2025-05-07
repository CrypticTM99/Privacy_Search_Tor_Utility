import sys
import time
import threading
import requests
import base64
from dns_over_https import DNSOverHTTPS
from malware_scanner.scan import scan_url_for_malware
from real_time_monitoring.ip_monitor import monitor_ip_changes
from real_time_monitoring.tor_health import monitor_tor_connection
from dashboard.dashboard import launch_dashboard

# DNS over HTTPS setup (Cloudflare)
doh_resolver = DNSOverHTTPS("https://cloudflare-dns.com/dns-query")

def query_dns_over_https(domain):
    try:
        response = doh_resolver.query(domain)
        print(f"DNS over HTTPS response for {domain}: {response}")
        return response
    except Exception as e:
        print(f"Error with DoH request: {e}")
        return None

def get_tor_exit_node_country():
    try:
        response = requests.get("https://check.torproject.org/api/ip")
        data = response.json()
        country = data.get("Country", "Unknown")
        print(f"Your Tor exit node is from: {country}")
        return country
    except Exception as e:
        print(f"Error fetching Tor exit node country: {e}")
        return None

def main():
    print("Safe Browser App started...")
    
    # Launch privacy dashboard in a separate thread
    dashboard_thread = threading.Thread(target=launch_dashboard)
    dashboard_thread.start()

    # Real-time monitoring: IP and Tor health checks
    ip_monitor_thread = threading.Thread(target=monitor_ip_changes)
    tor_health_thread = threading.Thread(target=monitor_tor_connection)
    ip_monitor_thread.start()
    tor_health_thread.start()

    # Example usage of DNS over HTTPS
    query_dns_over_https("example.com")

    # Example usage of Tor exit node country check
    get_tor_exit_node_country()

    # Scan a URL for malware (example usage)
    malware_check = scan_url_for_malware("http://example.com")

    # Wait for threads to finish
    ip_monitor_thread.join()
    tor_health_thread.join()
    dashboard_thread.join()

if __name__ == "__main__":
    main()
