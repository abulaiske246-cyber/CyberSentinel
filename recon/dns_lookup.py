import socket

def dns_lookup():
    hostname = input("Enter hostname: ")

    try:
        ip_address = socket.gethostbyname(hostname)
        print(f"IP address: {ip_address}")

    except socket.gaierror:
        print("DNS lookup failed. Unable to resolve hostname.")

if __name__ == "__main__":
    dns_lookup()
