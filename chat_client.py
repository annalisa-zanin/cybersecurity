import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"\n{message}")
        except:
            print("[!] Connection lost.")
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        if message:
            client_socket.send(message.encode('utf-8')) 
            # UTF-8 is a universal standard for encoding text. 
            # It is compatible with many languages and platforms, ensuring consistent interpretation of text on the receiver's side.
            # If another encoding format (e.g., ASCII) were used, some special characters (like accented letters) might be lost.

# Function to connect to the server and start the threads for sending and receiving
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))  # Connect to the local server

    print("[*] Connected to the server!")

    # Start threads for sending and receiving messages
    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_thread = threading.Thread(target=send_messages, args=(client_socket,))
    send_thread.start()

if __name__ == "__main__":
    start_client()