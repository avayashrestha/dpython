IP = input("Please enter the Target IP: ")
ports_input = input("Enter ports to scan (Seorate using commas ','): ")
ports = [int(port.strip()) for port in ports_input.split(",")]

services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL"
}

for port in ports:
    service = services.get(port, "unknown services")
    print(f"Scanning {IP} on port {port}... Possible Service: {service}")