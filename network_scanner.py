import socket
import threading

# Function to scan a port on a specific IP
def scan_port(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((ip, port))
        print(f"[+] Open port found on {ip}:{port}")
    except:
        pass
    finally:
        s.close()

# Function to find devices on the network
def find_devices(network):
    print(f"Scanning the network {network}...")
    for i in range(1, 255):
        ip = f"{network}.{i}"
        try:
            socket.gethostbyaddr(ip)
            print(f"[+] Device found: {ip}")
        except:
            pass

# Main function to run the program
def main():
    network = input("Enter the network (e.g., 192.168.1): ")
    find_devices(network)

    target_ip = input("Enter the IP of the device to analyze: ")
    common_ports = [21, 22, 23, 80, 443, 8080]  # FTP, SSH, HTTP, HTTPS...
    for port in common_ports:
        threading.Thread(target=scan_port, args=(target_ip, port)).start()

# Check if the script is being run directly
if __name__ == "__main__":
    main()