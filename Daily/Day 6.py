ip = input("Enter the User IP address: ")
while True:
    try:
        port = int(input("Enter target port: "))
        break
    except Exception as e:
        print("Something went wrong:", e)
print(f"Target acquired: {ip} on port {port}")