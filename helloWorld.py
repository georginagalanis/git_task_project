def is_valid_name(name):
    return not any(char.isdigit() for char in name) and len(name) > 0

name = input("What is your name? ")
while (not is_valid_name(name)):
    print("Names cannot contain numbers and must be at least one character long\n")
    name = input("What is your name? ")

print(f"Hello {name}")