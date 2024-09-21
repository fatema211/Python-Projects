# Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?"))
letter = ""

if nr_letters < 5:
    letter = random.choice(letters)
    print(letter)
    print(type(letter))

elif nr_letters >= 52:
    print("You can't have more than 52 letters in your password")
symbol = ""
nr_symbols = int(input(f"How many symbols would you like?"))
if nr_symbols < 7:
    symbol = random.choice(symbols)
    print(symbol)


else:
    print("You can't have more than 2 symbols in your password")

nr_numbers = int(input(f"How many numbers would you like?"))
number = ""
if nr_numbers < 7:
    number = random.choice(numbers)
    print(number)
    print(type(number))

print("Your password is " + letter + symbol + number)
print(letter)

# 
