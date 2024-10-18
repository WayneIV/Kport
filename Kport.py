import socket
from datetime import datetime


target = input("Enter the target IP or hostname: ")
start_port = int(input("Enter the starting port: "))
end_port = int(input("Enter the ending port: "))


print("-" * 50)
print(f"Starting scan on target: {target}")
print(f"Time started: {str(datetime.now())}")
print("-" * 50)


def port_scan(target, start_port, end_port):
    try:
        for port in range(start_port, end_port + 1):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: Open")
            sock.close()
    except KeyboardInterrupt:
        print("\nExiting Program...")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nServer not responding.")


port_scan(target, start_port, end_port)

print("-" * 50)
print(f"Scan completed at: {str(datetime.now())}")
print("-" * 50)
