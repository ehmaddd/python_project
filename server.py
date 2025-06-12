import socket
from datetime import datetime

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

HOST = '127.0.0.1'
PORT = 65432

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"{timestamp()} Server listening on {HOST}:{PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"{timestamp()} Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data or data.decode().lower() == 'exit':
                    print(f"{timestamp()} Client disconnected.")
                    break
                print(f"{timestamp()} Received: {data.decode()}")
                conn.sendall(data)
except Exception as e:
    print(f"{timestamp()} Server error: {e}")
