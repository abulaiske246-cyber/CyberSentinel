import socket

target = "127.0.0.1"
start_port = int(input("Enter starting port: "))
end_port = int(input("Enter ending port: "))

open_ports = []

for port in range(start_port, end_port + 1):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)

    result = sock.connect_ex((target, port))

    if result == 0:
        print(f"port {port} is OPEN")
        open_ports.append(port)
    else:
        print(f"port {port} is CLOSED")

    sock.close()

print("\nScan complete.")

if open_ports:
    print("Open ports:")
    for port in open_ports:
        print(f"  - {port}")
else:
    print("No open ports found.")
