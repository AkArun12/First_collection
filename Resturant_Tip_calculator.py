#Simple Billing system:

from typing import final
from xml.etree.ElementPath import prepare_predicate


print('Welcome to the Morad Resurant !!!')
print('**********************************')

print('MENU SET: \n Rice 1Bowl =100 Rs\n Meat 1 Plate=200Rs')

rice=input('How many plate do you need rice? :')
if rice=='1':
    rice_price=float(100)
else:
    rice_price=float(200)
meat=input('How many plate do you need Chicken Curry11? :')
if meat=='1':
   meat_price=float(200)
else:
    meat_price=float(350)
total=float(rice_price +meat_price)

total_bill=print(f'The total bill is:{total}')

tips=float(input('How much % tip do you want to pay? '))
percentage_tip= total*tips/100

final_total_bill= total+percentage_tip


print(f'Your final  total bill  after adding Tip is : {final_total_bill }')
choice=input('Do you want to divide your bills (yes/no):')
if choice in ('yes','no'):
    if choice=='yes':
        print(f'How many people do you want to divide with?')
        b=int(input('enter the number of people :'))
        per_person=final_total_bill/b
        #per_person="{:.2f}".format(final_total_bill/b) if we need 2 digit after decimal.
        print(f'The per person bill is {per_person}')

    else:
        print('Any one can pay the full bills  alone.')

      
print('Thanks for visiting us. See you again.')
         
    
    








