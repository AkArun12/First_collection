#Python code to calculate Love score:
print('WELCOME TO THE LOVE SCORE ERA...')
print('  ')
boy_name=input('Enter the boy name :')
girl_name=input('Enter girl name: ')

combined_string=boy_name+girl_name

lower_letter=combined_string.lower()

t=lower_letter.count('t')
r=lower_letter.count('r')
u=lower_letter.count('u')
e=lower_letter.count('e')
true=t+r+u+e


l=lower_letter.count('l')
o=lower_letter.count('o')
v=lower_letter.count('v')
e=lower_letter.count('e')

love=l+o+v+e


love_score=int(str(true)+str(love))

if (love_score) <10 or (love_score)>=90:
    print(f"Your love score{love_score}%. And it's  amazing.")
elif (love_score)>10 and (love_score)<=50:
    print(f"Your Love score is {love_score}% . And it's alright. ")
    
elif (love_score)>50 and (love_score)<90:
    print(f"Your Love score is {love_score}% . And it's wow. ")
else:
    print('good luck')
