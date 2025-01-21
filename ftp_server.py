import socket
import os
from datetime import datetime

# Function to save the received file
def save_file(client_socket):
    # Receive the filename
    filename = client_socket.recv(1024).decode('utf-8')
    print(f"Receiving file: {filename}")

    # Add a timestamp to the filename to make it unique
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    new_filename = f"received_{timestamp}_{filename}"

    # Save the file with the new name
    with open(new_filename, 'wb') as f: 
        # wb = Write Binary (because the file could be anything. An image, a pdf file, etc.)
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)  # Write data to the file
    print(f"File {filename} received and saved as {new_filename}.")

def start_server():
    # Create a socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to an address and port
    server_socket.bind(('0.0.0.0', 12345))  # Listen on all network interfaces, port 12345

    # Start listening for incoming connections
    server_socket.listen(5)
    print("Server is listening on port 12345...")

    while True:
        # Accept an incoming connection
        client_socket, client_address = server_socket.accept()
        print(f"Connection established with {client_address}")

        # Call the function to receive and save the file
        save_file(client_socket)

        # Close the connection after receiving the file
        client_socket.close()

if __name__ == "__main__":
    start_server()