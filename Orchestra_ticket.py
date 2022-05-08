#Python program for Orchestar Ticket based on height and Age.
print('Hello Welcome to our Function !!!')
height=int(input('Enter your height :'))
bill=0
count=3
if height>=120:
    print('Congrats!.You can ride but let me check your age and fees.')
    age=int(input('Enter your Age :'))

    if age<12:
        bill=5
        print('The entry fee is 5$')
    elif age>12 and age<18:
        bill=7
        print('The entry fee is 7$')
    elif age>=45 and age<=55:
        bill=0
    else:
        bill=12
        print('The entry fee is 12$')

    wants_photos=input('Do you want photos or not. The price is 3$.(yes/no) :')
    if wants_photos in ('yes','no'):
        if wants_photos=='yes':
            bill=bill+3
            

    print(f'your final bill is {bill} $.')
    
         
   

    print(' ')
    print('Thanks for Visiting us. Have a good day.!')

else:
    print(f'Your height is less  than  120. you cannot ride.')