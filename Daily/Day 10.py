import time

file = open("target.txt", "a")
file.write("Inserted IP")

i = 1
while i <= 3:
    ip = input("Enter IP address: ")
    time.sleep(0.2)
    print(f"Scanning target: {ip}...")
    time.sleep(0.5)
    file.write(f"\n{ip}")
    i += 1

file.write("\nScan Completed!")
file.close()

print("Stopping the code...")
time.sleep(1)
