def is_valid_name(name):
    return not any(char.isdigit() for char in name)

name = input("What is your name? ")
while (not is_valid_name(name)):
    print("Names cannot contain numbers\n")
    name = input("What is your name? ")

print(f"Hello {name}")