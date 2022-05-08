import random
friends=input('Enter friends name seperated with comma .')
friends_name=friends.split(',')
print(friends_name)
num_friends=len(friends_name)
print(f'The total number of friends is {num_friends}.')
random_choice=random.randint(0,num_friends-1)
print(f'computer selectd:  {random_choice}')

who_pay=friends_name[random_choice]

print(who_pay+'is going to pay.')