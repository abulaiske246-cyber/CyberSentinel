import socket

def run_scanner():
    target = "127.0.0.1"
    try:
        start_port = int(input("Enter starting port: "))
        end_port = int(input("Enter ending port: "))
    except ValueError:
        print("Invalid port number. Please enter numbers only.")
        return

    if not (1 <= start_port <= 65535) or not (1 <= end_port <= 65535):
        print("Invalid port range. Ports must be between 1 and 65535.")
        return

    if start_port > end_port:
        print("Invalid port range. Starting port must be less than or equal to ending port.")
        return

    open_ports = []

    print(f"\nStarting scan on {target}")
    print(f"Scanning ports {start_port}-{end_port}...\n")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

        sock.close()

    print("\nScan complete.")

    if open_ports:
        print("Open ports:")
        for port in open_ports:
            print(f"  - {port}")
    else:
        print("No open ports found.")

if __name__ == "__main__":
    run_scanner()
