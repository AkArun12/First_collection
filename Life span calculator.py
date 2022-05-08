#Python code to calculate Age in our life.////
print('Hello Morad Hosan. We are here to calculate your remaining life span..')

max_age=int(input('Enter the maximum age up to which you will survive :'))
current_age=int(input('Enter your current Age: '))

remaining_year= max_age-current_age
remaining_month= remaining_year*12
remaining_week=remaining_month*4
remaining_days= remaining_week *7

print(f'Mr.Morad: you have altogether, In term of days {remaining_days} days left ,In term of month {remaining_month} months left and in term of years {remaining_year} years left.')
print('wish you happy and long life ahead..')