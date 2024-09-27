# A password generator

import random

letters = ["a", "b", "c", "G", "U", "Z", "V",  "d", "e", "f", "g", "h", "i", "j" ]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
characters = ["@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "-"]

char_ = int(input("How many characters would you want in your password?: "))
numb_ = int(input("How many numbers would you want in your password?: "))
let_ = int(input("How many letters would you want in your password?: "))

# let's assume all the inputs are 4 (you can use different numbers for each input)
password_list = []

for i in range(0, char_):
    password_list.append(random.choice(characters))

for i in range(0, numb_):
    password_list.append(random.choice(numbers))

for i in range(0, let_):
    password_list.append(random.choice(letters))

random.shuffle(password_list)


your_password = ""
for i in password_list:
    your_password += i

print(your_password)





