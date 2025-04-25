username = ['admin', 'agent', 'user']
password = ['1234', '5678', 'abcd', 'hacktheworld']

correct_user = input("Enter username: ")
correct_pass = input("Enter password: ")

found = False

for user in username:
    for pwd in password:
        print(f"Typing {user}: {pwd}")
        if user == correct_user and pwd == correct_pass:
            print(f"Access granted for {user}.")
            found = True
            break
    if found:
        break

if not found:
    print("Access denied.")