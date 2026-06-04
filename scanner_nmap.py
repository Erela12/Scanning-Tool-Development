import nmap
scanner = nmap.PortScanner()
target = input("Enter target IP: ")
scanner.scan(target, "1-100")
for host in scanner.a11_hosts():
    print(f"\nHost: {host}")
    for proto in scannner[host].all_protocols():
        ports = scanner[host][proto].keys()
        for port in ports:
            state = scanner[host][proto][port]['state']
            print(f"Port {port}: {state}")
