import random


print("Welcome to the PyPassword Generator!")
how_many_letters = int(input("How many letters would you like in your password? "))      
how_many_numbers = int(input("How many numbers would you like in your password? ")) 
how_many_specials = int(input("How many special signs would you like in your password? ")) 

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

specials = ['!','@','#','$','%','^','&','*','(',')','-','_','?','.']

chosen_letter = ''
chosen_number = 0
chosen_special = ''

for letter in range(how_many_letters):
    chosen_letter += random.choice(letters)
    
    
for number in range(how_many_numbers):
    chosen_number += random.choice(numbers)
    
    
for special in range(how_many_specials):
    chosen_special += random.choice(specials)
    
password = chosen_letter + chosen_special + str(chosen_number)
password = ''.join(random.sample(password,len(password)))

print(f"Your password is: {password}")