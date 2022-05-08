# #Python passward generator:
import random
from typing import final
print('Welcome to the password generator.')
print('Important note!!!! \nYour password must contain letter,number and symbols.')
print(' ')


letters=['A','B','C','D','E','F','G','H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R','S','T','U','V','W','X','Y',' Z','a', 'b', 'c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','@','#','$','%','&','*','+',',']

nr_letters=int(input('How many letters do you want in your password :'))
nr_numbers=int(input('How many mumbers do you want in your password :'))
nr_symbols=int(input('How many symbols do you want in your password :'))

password=''

for char in range(1,nr_letters+1):
    random_char=random.choice(letters)
    password=password+random_char


for num in range(1,nr_numbers+1):
    random_num=random.choice(numbers)
    password=password+random_num



for sym in range(1,nr_symbols+1):
    random_sym=random.choice(symbols)
    password=password+random_sym


print(f'The generated password is {password} .')

#From here, we have same password with same characters, symbol and number  but its shuffled. Its more secure.!


shuffled_pass= ''.join(random.sample(password,len(password)))
print(f'The shuffled password is :{shuffled_pass}')







