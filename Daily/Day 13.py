domain_name = input("Please enter Domain name (eg: example.com): ")
subdomain = ["admin", "mail", "dev", "login", "shop", "media", "access", "studio", "music", "blog", "detalils", "home"]

for sub in subdomain:
    full_url = f"{sub}.{domain_name}"
    print(f"Scanning: {full_url}")