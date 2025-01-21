# Cybersecurity Exercises

This repository contains a set of exercises focused on cybersecurity topics, particularly related to networks and vulnerability assesment.

### Prerequisites
Before running the scripts, make sure you have the following installed:
- Python 3.x
- Necessary Python libraries (`socket`, `argparse`, etc.)
- A Bash-compatible terminal for running the `.sh` script (i.e. GitBash for Windows)

# Repository Structure
## Network Scanning Exercise
This exercise demonstrates the basics of network communication, including how sockets and addressing work within a network.
The program scans a target IP address to identify which ports are open on devices in the network. It uses Python's socket module to attempt connections to common ports and reports their status (open or closed).
- `execute_network_scanner.sh`: A Bash script to execute the network_scanner.py Python script with predefined or user-specified parameters.
- `network_scanner.py`: A Python script for scanning a network to discover devices by their IP addresses and to identify open ports on a given target device.
## Chat Simulation Exercise
This exercise demonstrates how communication between a server and multiple clients works.
- `chat_server.py`: A Python script implementing the logic of a server that receives messages from clients and broadcasts those messages to all other connected clients.
- `chat_client.py`: A Python script implementing the logic of a client that can send messages to, and receive messages from, the server.
## File Transfer (FTP) Exercise
This exercise demonstrates how a server can receive and save files sent from a client over a network connection.
- `ftp_server.py`: A Python script implementing the logic of a server that listens for incoming file transfers from clients, receives the file, and saves it with a timestamped name.
- `ftp_client.py`: A Python script implementing the logic of a client that sends a file to the server for storage.

## Network Scanning Exercise

### How to Use

#### 1. Clone the Repository
To clone this repository to your local machine, run the following command:
```bash
git clone https://github.com/annalisa-zanin/cybersecurity.git
```

#### 2. Make the Bash Script Executable
To run the execute_network_scanner.sh script, you'll need to grant execution permissions to the file. You can do this by running the following command:
```bash
chmod +x execute_network_scanner.sh
```

#### 3. Run the Network Scanner
Once the Bash script is executable, you can run it with the following command:
```bash
./execute_network_scanner.sh
```
Alternatively, you can run the Python script directly using Python:
```bash
python3 network_scanner.py
```
#### 4. Security Considerations
Be cautious when using network scanning tools, as they can trigger alarms in intrusion detection systems (IDS) or be considered malicious activity on networks that you do not own or have permission to scan. Always ensure you have authorization before performing any network scans.

## Chat Simulation Exercise
### How to Use

#### 1. Clone the Repository
To clone this repository to your local machine, run the following command:
```bash
git clone https://github.com/annalisa-zanin/cybersecurity.git
```

#### 2. Run the Chat Server
First, start the chat server by running the following command in your terminal:
```bash
python3 chat_server.py
```
The server will listen for incoming connections from clients on all network interfaces (`0.0.0.0`) and port `12345` by default. You can modify the script to change the port if needed.

#### 3. Run the Chat Client
Next, open a new terminal window and start a chat client with the following command:
```bash
python3 chat_client.py
```
The client will connect to the server at `127.0.0.1` (localhost) and port `12345` by default. Ensure the server is running before starting the client. You can start multiple clients to simulate a group chat.

#### 4. Security Considerations
When running this exercise:
- Ensure the server is running in a secure environment, as it accepts connections from any client on the specified port.
- Avoid exposing the server to untrusted networks unless additional security measures, such as authentication or encryption, are implemented.
- Be mindful of network activity; excessive testing may generate unwanted traffic.

## File Transfer (FTP) Exercise
### How to Use

#### 1. Clone the Repository
To clone this repository to your local machine, run the following command:
```bash
git clone https://github.com/annalisa-zanin/cybersecurity.git
```
#### 2. Run the FTP Server
First, start the FTP server by running the following command in your terminal:
```bash
python3 ftp_server.py
```
The server will listen for incoming connections from clients on all network interfaces (`0.0.0.0`) and port `12345` by default. You can modify the script to change the port if needed.

#### 3. Run the FTP Client
Next, open a new terminal window and start an FTP client with the following command:
```bash
python3 ftp_client.py
```
The client will connect to the server at `127.0.0.1` (localhost) and port `12345` by default. Ensure the server is running before starting the client. The client can send a file to the server for storage.

#### 4. Security Considerations
When running this exercise:
- Ensure the server is running in a secure environment, as it accepts connections from any client on the specified port.
- Avoid exposing the server to untrusted networks unless additional security measures, such as authentication or encryption, are implemented.
- Be mindful of network activity; excessive testing may generate unwanted traffic.