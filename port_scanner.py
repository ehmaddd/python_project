import socket
import time

def scan_port(host, port):
    try:
        # Create a socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout to avoid hanging
        
        # Attempt to connect to the port
        result = sock.connect_ex((host, port))
        
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED")
        
        sock.close()
    
    except socket.error:
        print(f"Error scanning port {port}")
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
        exit()

def port_scanner():
    print("=== Simple Port Scanner ===")
    
    try:
        # Get user input with Ctrl+C handling
        try:
            host = input("Enter target host (e.g., 'localhost' or 'scanme.nmap.org'): ")
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))
        except KeyboardInterrupt:
            print("\n\n[!] Scan canceled by user during input.")
            return  # Exit gracefully
        
        print(f"\nScanning {host} from port {start_port} to {end_port}...")
        
        # Scan ports with Ctrl+C handling
        try:
            for port in range(start_port, end_port + 1):
                scan_port(host, port)
                time.sleep(0.2)  # Ethical delay
        except KeyboardInterrupt:
            print("\n\n[!] Scan canceled by user during execution.")
    
    except ValueError:
        print("[!] Error: Invalid port number (must be integers).")
    except Exception as e:
        print(f"[!] Unexpected error: {e}")

if __name__ == "__main__":
    port_scanner()