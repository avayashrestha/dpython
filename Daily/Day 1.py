# The day 1
name = input("Enter your name agent:  ")
print("Hello", name, "Welcome to the world of hacking")

tool = input("What's your favouriate hacking tools:  ")
print(f'Ah {tool} is a great tool, I love it too')

age = int(input(f"What's your age {name}:  "))

if age < 18:
    print("This is perfectly fine, you are still a kid")
elif age <=8:
    print("That's the spirit, you are a genius")
else:
    print("Welcome to the world of hacking")