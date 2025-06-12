import socket

def start_client():
    # Create a TCP/IP socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Define server address and port
    server_address = ('localhost', 12345)
    
    try:
        # Connect to the server
        print(f"Connecting to {server_address[0]}:{server_address[1]}")
        client_socket.connect(server_address)
        
        while True:
            # Get user input
            message = input("Enter message to send (or 'exit' to quit): ")
            if message.lower() == 'exit':
                break
            
            # Send message to server
            client_socket.sendall(message.encode())
            
            # Receive response from server
            response = client_socket.recv(1024).decode()
            print(f"Server response: {response}")
    
    except ConnectionRefusedError:
        print("Error: Server is not running.")
    
    finally:
        # Close the connection
        client_socket.close()
        print("Connection closed")

if __name__ == "__main__":
    start_client()