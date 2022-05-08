#Python code for Pizza Resturant:
print('*****************************************************')
print("Welcome to Morad'S pizza resturant !!!")
print('-----------------------------------------------------')

while True:
    pizza_size=input('Select the pizza size: (Small:S, Medium:M or Large:L :')

    if pizza_size=='S':
        bill=15 
    elif pizza_size=='M':
        bill=20

    elif pizza_size=='L':
        bill=25

    need_pepperoni=input('Do you need pepperoni? (yes/no) :')
    if need_pepperoni=='yes':
        if pizza_size=='S':
            bill=bill+2
        else:
            bill=bill+3

        need_cheese=input('Do you need cheese? (yes/no):')
        if need_cheese=='yes':
            bill=bill+1
            print(f'your Total bill is {bill}$.')
            
        else:
            print(f'Your Total bill is {bill}$.')
            print('Thanks for shopping..')

    shop_again=input('Do you want to shop again? yes/no: ')
    if shop_again=='yes':
        continue
    else:
        print('Thanks for shopping with us.')
        break
         
print('Have a good Day.')
           
        





        