import socket
from datetime import datetime

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"{timestamp()} Connected to server at {HOST}:{PORT}")
        try:
            while True:
                message = input("Enter message ('exit' to quit): ")
                s.sendall(message.encode())
                if message.lower() == 'exit':
                    print(f"{timestamp()} Disconnected from server.")
                    break
                data = s.recv(1024)
                print(f"{timestamp()} Server replied: {data.decode()}")
        except KeyboardInterrupt:
            print(f"\n{timestamp()} Client interrupted with Ctrl+C. Disconnecting gracefully.")
            try:
                s.sendall("exit".encode())  # Notify server of disconnection
            except:
                pass
except ConnectionRefusedError:
    print(f"{timestamp()} Connection failed: Server is not running.")
except Exception as e:
    print(f"{timestamp()} Client error: {e}")
