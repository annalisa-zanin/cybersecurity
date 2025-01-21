import socket

# Funzione per inviare un file al server
def send_file(filename, server_ip, server_port):
    # Crea un socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connessione al server
    client_socket.connect((server_ip, server_port))

    # Invia il nome del file
    client_socket.send(filename.encode('utf-8'))

    # Invia il contenuto del file in blocchi da 1024 byte
    with open(filename, 'rb') as f: 
        # rb = Read Binary (because the file could be anything. An image, a pdf file, etc.)
        while (chunk := f.read(1024)):
            client_socket.send(chunk)

    print(f"File {filename} sent successfully.")
    client_socket.close()

if __name__ == "__main__":
    # Inserisci il nome del file che vuoi inviare
    filename = input("Enter the filename to send: ")
    # Inserisci l'IP del server (in questo caso, il server è locale)
    server_ip = input("Enter server IP (e.g., 127.0.0.1): ")
    server_port = 12345

    send_file(filename, server_ip, server_port)