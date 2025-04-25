def get_target_info():
    ip = input("Enter the target IP address: ")
    domain = input("Enter the target domain: ")
    return ip, domain

def is_common_port(port):
    common_ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306]
    return port in common_ports

def check_port(port):
    if port == 22:
        return "SSH"
    
    elif port == 80:
        return "HTTP"
    elif port == 3306:
        return "MySQL"
    else:
        return "Unknown Service"
    
def show_summary(ip, domain, port, service):
    print("\n Target Recon Summary:")
    print(f"IP Address: {ip}")
    print(f"Domain: {domain}")
    print(f"Port: {port} ({service})")
    print(f"Port Status: {'Open' if service != 'Unknown Service' else 'Closed'}")
    print(f"Common Port: {'Yes' if is_common_port(port) else 'No'}")

# use the functions
ip, domain = get_target_info()
port = int(input("Enter the target port: "))
service = check_port(port)
show_summary(ip, domain, port, service)