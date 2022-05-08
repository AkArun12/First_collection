
while True:
    def prime_num():
        a=int(input('Enter the number :'))
        is_prime=True
        for i in range(2,a):
            if a%i==0:
                is_prime=False
        if is_prime:
            print('Its  a prime')
        else:
            print('Its not a prime')

    prime_num()

    check_again=input('Do you want to check again?(yes/no:)')
    if check_again=='yes':
        continue
    else:
        break
