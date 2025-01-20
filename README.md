# Cybersecurity Exercises

This repository contains a set of exercises focused on cybersecurity topics, particularly related to network scanning and vulnerability assessment.

## Repository Structure
## NETWORK SCANNING EXERCISE
- `execute_network_scanner.sh`: A Bash script that executes the `network_scanner.py` Python script.
- `network_scanner.py`: A Python script for scanning a network, given its IP address, and for scanning the open ports of a device identified by its IP address.

## NETWORK SCANNING EXERCISE
## Prerequisites
Before running the scripts, make sure you have the following installed:
- Python 3.x
- Necessary Python libraries (`socket`, `argparse`, etc.)
- A Bash-compatible terminal for running the `.sh` script (i.e. GitBash for Windows)

## How to Use

### 1. Clone the Repository
To clone this repository to your local machine, run the following command:
```bash
git clone https://github.com/annalisa-zanin/cybersecurity.git
```

### 2. Make the Bash Script Executable
To run the execute_network_scanner.sh script, you'll need to grant execution permissions to the file. You can do this by running the following command:
```bash
chmod +x execute_network_scanner.sh
```

### 3. Run the Network Scanner
Once the Bash script is executable, you can run it with the following command:
```bash
./execute_network_scanner.sh <target-ip>
```
Replace <target-ip> with the IP address of the target device or network you want to scan.
Alternatively, you can run the Python script directly using Python:
```bash
python3 network_scanner.py
```

### 4. Scan Details
The network_scanner.py script will scan the target IP address to check which ports are open on the device.
It uses the socket module to attempt connections to common ports and report their status (open or closed).

### 5. Security Considerations
Be cautious when using network scanning tools, as they can trigger alarms in intrusion detection systems (IDS) or be considered malicious activity on networks that you do not own or have permission to scan. Always ensure you have authorization before performing any network scans.
