from cx_Freeze import setup, Executable
import os

# This will define the path for the entire project(SafeSearchBrowser folder)
base_path = os.path.dirname(os.path.abspath(__file__))  # This ensures the paths are relative to the SafeSearchBrowser folder

# This will be the necessary files to include in the build
include_files = [
    os.path.join(base_path, "scanner", "malware_scanner.py"),  # malware_scanner.py
    os.path.join(base_path, "real-time-monitoring", "ip_monitor.py"),  # ip_monitor.py
    os.path.join(base_path, "real-time-monitoring", "tor_health.py"),  # tor_health.py
    os.path.join(base_path, "dashboard", "dashboard.py"),  # dashboard.py
    os.path.join(base_path, "ml", "risk_model.py"),  # risk_model.py
    os.path.join(base_path, "assets"),  # assets folder
]

# Setup cx_Freeze configuration
setup(
    name="SafeBrowserSearch",
    version="1.0",
    description="Safe Browser Search Application",
    options={
        "build_exe": {
            "packages": [
                "requests", "dns_over_https", "pycryptodome", "stem", "psutil", "logging", "collections.abc",
                "malware_scanner", "real_time_monitoring", "dashboard", "ml",  # Include the necessary modules
            ],
            "include_files": include_files  # Include the necessary files and folders
        }
    },
    executables=[Executable("main.py", base=None, target_name="SafeBrowserSearch.exe")]  # No icon specified
)
