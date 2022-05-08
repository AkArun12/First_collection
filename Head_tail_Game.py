#Simple python program for Head/Tail Guessing game.
import random
while True:
    print('Welcome to Head_Tail Game !!!!')
    print('   ')

    user_choice=input('Enter yor choice head or tail :')
    computer_choice=random.choice(['head','tail'])
    print('  ')

    print(f'You have choosen: {user_choice} \nand computer has choosen:{computer_choice}')
    if user_choice==computer_choice:
        print('Its a tie game.')

    elif user_choice=='head' and computer_choice=='tail':
        print('you win.')

    elif user_choice=='tail' and computer_choice=='head':
        print('Computer win the game.')
 

    play_again=input('Do yo want to play again? (yes/no):')
    if play_again=='yes':
        continue
    else:
        break

print('Thanks for playing Game.')
