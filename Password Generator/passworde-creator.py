import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the Password Generator!')

nr_latters = int(input('How many Letters would you like in your password?\n'))
nr_symbols = int(input('How many Symbols would you like?\n'))
nr_numbers = int(input('How many Numbers would you like?\n'))

password_lists = []

for char in range(1, nr_latters + 1):
    password_lists.append(random.choice(letters))

for char in range(1, nr_numbers + 1):
    password_lists.append(random.choice(numbers))

for char in range(1, nr_symbols + 1):
    password_lists.append(random.choice(symbols))

random.shuffle(password_lists)

password = ""

for char in password_lists:
    password += char

print(f"Your password is: {password}")