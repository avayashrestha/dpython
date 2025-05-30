# Ask user for target info
ip = input("Enter target IP: ")
domain = input("Enter target Domain: ")
port = int(input("Enter target port: "))
service = input("Enter service running on this port: ")
os = input("Enter the OS you want to use: ")
status = input("The current status of the target: ")

# Store in a dictionary
target = {
    "ip": ip,
    "domain": domain,
    "port": port,
    "service": service,
    "OS": os,
    "Status": status,
}

# Print target info
print("\nTarget Info:")
print(f"IP Address: {target['ip']} ({target['domain']})")
print(f"Port: {target['port']}")
print(f"Service: {target['service']}")
print(f"Operating system: {target['OS']}")
print(f"Status: {target['Status']}")
