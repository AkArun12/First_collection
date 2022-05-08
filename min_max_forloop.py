# program to calculate lowest and highest number from a list:

a=[22,44,33,89,56,12]

max_value=0
min_value=a[0]

for marks in a:
    if max_value<marks:
        max_value=marks
print(f'The max value is {max_value} .')


for marks in a:
    if min_value>marks:
        min_value=marks
print(f'The minimum value in list is {min_value} .')
