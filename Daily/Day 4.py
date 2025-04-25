password = input("Enter the password: ")

# Common passwords list
common = ["password", "123456", "123456789", "12345678", "12345", "1234567", "qwerty", "abc123", "password1", "111111", "123123", "admin", "letmein", "welcome", "monkey", "iloveyou", "trustno1", "dragon", "sunshine", "1234"]

# Get the user’s custom password list
raw_data = input("Please enter the password list (separate by commas): ")
data = raw_data.split(",")

# Combine common passwords with the user-provided list
wordlist = common + data

# Attempt counter
attempts = 0

# Brute-force attempt
for pwd in wordlist:
    attempts += 1
    print(f"Attempt {attempts}: {pwd}")
    if pwd == password:
        print(f"Password is correct! It took {attempts} attempts.")
        break
else:
    print("Password is incorrect.")
