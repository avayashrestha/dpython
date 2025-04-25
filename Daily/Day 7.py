# System 

common_password = ["admin", "1234", "letmein"]
pass_input = input("Please write a set of password seprated by ','")
password = [pwd.strip() for pwd in pass_input.split(",")]
wordlist = common_password + password

# Target Input 
userp = input("Please enter the password user: ")

# Password Guesser
i = 1
for pwd in wordlist:
    print(f"Attempt {i}: {pwd}")
    i += 1
    if pwd == str(userp):
        print(f"Correct password is {pwd} found in attempt {i}")
        break
else:
    print("Password Not Found")