
#BMI calculations:
# BMI= weight(kg)/height**2(m2)
def bmi():
    weight=float(input('Enter the weight in kg :'))
    height=float(input('Enter the height in metre :'))
    BMI=round(weight/height**2,2)
    
# Here we have make output up to two decimal position using round function.

    print(f'BMI for the weight {weight} kg  and height {height} metre is :{BMI}')

    if BMI<18.5:
        print(f'You are under weight. your BMI is : {BMI}')
        print('Keep eating healty foods more..')
    elif BMI>18.5 and BMI<25:
        print('You have Normal weight') 
        print('Good maintanence...')   
    elif BMI>25 and BMI<30:
        print(f'You are Overweighted .')
        print('You have to do Exercise alot.')
    elif BMI>30:
        print(f'You are Obese.')

bmi()
print('we wish you haapy life and Healty life. !!!')

    



 