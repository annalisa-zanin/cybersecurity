import socket
import threading

# List to keep track of connected clients
clients = []

# Function to handle communication with each client
def handle_client(client_socket, client_address):
    print(f"[+] New connection: {client_address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            # recv(1024) reads up to 1024 bytes from the socket's receive buffer in a single call.
            # Network data is often split into smaller packets, so reading in chunks avoids memory overuse.
            # 1024 bytes is a practical default, balancing efficiency and memory usage.
            if message:
                print(f"[{client_address}] {message}")
                # Forward the message to all other clients
                broadcast_message(message, client_socket)
            else:
                break
        except:
            break

    # Remove the client from the list and close the connection
    clients.remove(client_socket)
    client_socket.close()

# Function to send a message to all connected clients except the sender
def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                continue

# Function to start the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #SOCK_STREAM => TCP, AF_INET => IPv4
    server.bind(('0.0.0.0', 12345))
    # '0.0.0.0' means the server accepts connections on all available network interfaces of the machine.
    # This includes interfaces like Ethernet, Wi-Fi, or virtual network adapters (e.g., for virtual machines).
    # By specifying '0.0.0.0', the server becomes accessible from any IP address configured on the machine.
    server.listen(5)
    print("[*] Server is listening on port 12345...")

    while True:
        client_socket, client_address = server.accept()
        client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        client_thread.start()

if __name__ == "__main__":
    start_server()