blacklist = ["8.8.8.8", "1.1.1.1", "123.45.67.89"]

with open("target.txt", "r") as file:
    for line in file:
        ip = line.strip()
        lines = line.strip()

        print(f"Scanning IP: {ip}")

        if ip.startswith("192."):
            print("Private network IP found!")

        if ip in blacklist:
            print(f"Blacklisted ip found: {ip}")

    print(f"Scan Completed! Total targets scanned: {len(lines)}")