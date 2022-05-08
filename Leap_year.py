#Python code for leap year.
'''Conditions for Leap year:
1.If a year is exactly divisible by (400 or not exactly divisibel by 100)
 AND year is divisible by 4 then it is leap year.
 Here we have three cases.
'''
print('Hello, Welcome to the Leap year calculator. !')
print('   ')
year=int(input('Enter the year :'))
if ((year %400==0 )or (year %100!=0) and (year%4==0)):
    print(f'The inserted year {year} is leap year .')
else:
    print(f'The inserted year {year} is not a leap year.')
    print('A leap year must be exactly divisible by (400 or !divisible by 100 )AND  (divisible by 4)')
print(' ')
print('Thanks for calculating Leap year. keep learing.!!!')
