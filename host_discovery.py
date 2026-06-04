import socket
import os

hostname = socket.gethostname()

local_ip = socket.gethostbyname(hostname)

print("Hostname:", hostname)
print("Local IP:", local_ip)

parts = local_ip.split('.')

first_octet = int(parts[0])

if first_octet >= 1 and first_octet <= 126:
    print("IP Class: A")

elif first_octet >= 128 and first_octet <= 191:
    print("IP Class: B")

elif first_octet >= 192 and first_octet <= 223:
    print("IP Class: C")

else:
    print("Special or Unknown IP Class")

print("\nGateway Information:")

os.system("ip route | grep default")
