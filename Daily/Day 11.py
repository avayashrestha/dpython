count = 0

with open("target.txt", "r") as file:
    for line in file:
        ip = line.strip()
        print(f"Scanning IP: {ip}")
        count += 1
        if ip == "8.8.8.8":
            print("🛑 Alert! Suspicious Google DNS found!")

print(f"Total targets found: {count}")