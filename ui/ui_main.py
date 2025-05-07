import sys
import threading
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from real_time_monitoring.ip_monitor import monitor_ip_changes
from real_time_monitoring.tor_health import monitor_tor_connection
from malware_scanner.scan import scan_url_for_malware
from ml.risk_model import risk_assessment

class SafeBrowserApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Safe Browser Dashboard")
        self.setGeometry(300, 300, 600, 400)
        
        # Layout
        self.layout = QVBoxLayout()

        # Labels for displaying info
        self.ip_label = QLabel("IP Address: Not Set")
        self.tor_status_label = QLabel("Tor Status: Not Set")
        self.malware_status_label = QLabel("Malware Check: Not Scanned")
        self.risk_label = QLabel("Privacy Risk: Unknown")
        
        self.layout.addWidget(self.ip_label)
        self.layout.addWidget(self.tor_status_label)
        self.layout.addWidget(self.malware_status_label)
        self.layout.addWidget(self.risk_label)

        # Button to refresh system information
        self.refresh_button = QPushButton("Refresh")
        self.refresh_button.clicked.connect(self.refresh_data)
        self.layout.addWidget(self.refresh_button)

        self.setLayout(self.layout)

        # Start real-time monitoring in separate threads
        self.ip_monitor_thread = threading.Thread(target=monitor_ip_changes, args=(self.update_ip_label,))
        self.tor_monitor_thread = threading.Thread(target=monitor_tor_connection, args=(self.update_tor_status,))
        self.ip_monitor_thread.start()
        self.tor_monitor_thread.start()

        self.show()

    def update_ip_label(self, new_ip):
        self.ip_label.setText(f"IP Address: {new_ip}")

    def update_tor_status(self, status):
        self.tor_status_label.setText(f"Tor Status: {status}")

    def refresh_data(self):
        # Example of refreshing the UI with live data
        print("Refreshing data...")
        self.update_malware_check()
        self.update_risk_assessment()

    def update_malware_check(self):
        url = "http://example.com"  # Replace with dynamic URL
        is_malicious = scan_url_for_malware(url)
        self.malware_status_label.setText(f"Malware Check: {'Malicious' if is_malicious else 'Safe'}")

    def update_risk_assessment(self):
        user_behavior_data = {"ip_changes": 5, "tor_usage": True}  # Example data
        risk_score = risk_assessment(user_behavior_data)
        self.risk_label.setText(f"Privacy Risk: {risk_score}")

def start_ui():
    app = QApplication(sys.argv)
    window = SafeBrowserApp()
    sys.exit(app.exec_())

if __name__ == "__main__":
    start_ui()
