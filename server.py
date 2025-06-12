import socket

def start_server():
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_address = ('localhost', 12345)
    print(f"Starting server on {server_address[0]}:{server_address[1]}")
    server_socket.bind(server_address)
    
    # Listen for incoming connections (max 1 connection in queue)
    server_socket.listen(1)
    
    while True:
        print("Waiting for a connection...")
        connection, client_address = server_socket.accept()
        
        try:
            print(f"Connection established with {client_address}")
            
            while True:
                # Receive data from client (max 1024 bytes)
                data = connection.recv(1024).decode()
                if not data:
                    break
                print(f"Received from client: {data}")
                
                # Send a response back
                response = f"Server received: {data}"
                connection.sendall(response.encode())
        
        finally:
            # Clean up the connection
            connection.close()
            print("Connection closed")

if __name__ == "__main__":
    start_server()