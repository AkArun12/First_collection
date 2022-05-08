
even_total=0
odd_total=0
for x in range(1,101):
    if x%2==0:
        even_total=even_total+x
    
print(f'The sum of Even numbers between 1 to 100 is {even_total} .')



# for x in range(2,101,2):
#     even_total=even_total+x   
# print(f'The Even numbers between 1 to 100 is {even_total} .')




for y in range(1,101):
  
    if y%3==0:
        odd_total=odd_total+y

print(f'The sum of Odd numbers between 1 to 100 is {odd_total} .')
