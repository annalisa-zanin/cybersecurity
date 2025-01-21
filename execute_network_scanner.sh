#!/bin/bash

echo "Choose what you want to do:"
echo "1. Find devices on the network"
echo "2. Scan ports of a device"
read -p "Option: " option

if [ "$option" -eq 1 ]; then
    read -p "Enter the network (e.g., 192.168.1): " network
    python3 -c "import network_scanner; network_scanner.find_devices('$network')"
elif [ "$option" -eq 2 ]; then
    read -p "Enter target IP: " ip
    read -p "Enter port to scan: " port
    python3 -c "import network_scanner; network_scanner.scan_port('$ip', $port)"
else
    echo "Invalid option!"
fi