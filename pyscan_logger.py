import subprocess
import json
from datetime import datetime

# This script runs the scanner and saves the results to a JSON file
def run_scan():
    print("--- Starting Security Scan ---")
    
    # 1. Run the pyscan command
    result = subprocess.run(['pyscan'], capture_output=True, text=True, shell=True)
    
    # 2. Organize the data
    report_data = {
        "scan_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "tool_used": "Pyscan-RS",
        "scan_results": result.stdout
    }

    # 3. Save it to a JSON file
    with open('scan_report.json', 'w') as f:
        json.dump(report_data, f, indent=4)
    
    print("Success! Security report saved as 'scan_report.json'")

if __name__ == "__main__":
    run_scan()
