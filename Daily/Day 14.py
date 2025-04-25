# with open("found.txt", "w") as file:
#     file.write("data")


domain = input("Please enter a valid domain(eg. example.com): ")
subdomains = ["admin", "login", "media", "dev", "shop"]

with open("found.txt", "w") as file:
    for sub in subdomains:
        full = f"{sub}.{domain}"
        if "admin" in sub or "login" in sub:
            file.write(full + "\n")
            print(f"Scanning: {full} [FOUND]")
        else:
            print(f"Scanning: {full}")

