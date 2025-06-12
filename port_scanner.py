import socket
import time
from datetime import datetime

def timestamp():
    return datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))

        if result == 0:
            print(f"{timestamp()} Port {port} is OPEN")
        else:
            print(f"{timestamp()} Port {port} is CLOSED")
        
        sock.close()
    
    except socket.error:
        print(f"{timestamp()} Error scanning port {port}")
    except KeyboardInterrupt:
        print(f"\n{timestamp()} Scan aborted by user.")
        exit()

def port_scanner():
    print(f"{timestamp()} === Simple Port Scanner ===")
    
    try:
        # Get user input with Ctrl+C handling
        try:
            host = input("Enter target host (e.g., 'localhost' or 'scanme.nmap.org'): ")
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))
        except KeyboardInterrupt:
            print(f"\n{timestamp()} [!] Scan canceled by user during input.")
            return
        
        print(f"\n{timestamp()} Scanning {host} from port {start_port} to {end_port}...")

        try:
            for port in range(start_port, end_port + 1):
                scan_port(host, port)
                time.sleep(0.2)
        except KeyboardInterrupt:
            print(f"\n{timestamp()} [!] Scan canceled by user during execution.")
    
    except ValueError:
        print(f"{timestamp()} [!] Error: Invalid port number (must be integers).")
    except Exception as e:
        print(f"{timestamp()} [!] Unexpected error: {e}")

if __name__ == "__main__":
    port_scanner()
