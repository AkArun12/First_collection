print('##############################################################')
print('welcome to Rock, paper and Scissor Game !')
print(' ')

import random
while True:
    user_choice=input('Select rock , paper or scissor :')
    

    possible_actions=['rock','paper','scissor']
    computer_choice=random.choice(possible_actions)


    print(f'you chooses {user_choice}. \nComputer chooses {computer_choice}.')

    if user_choice in possible_actions:
        if user_choice==computer_choice:
            print("It'a Tie Game.")

        elif user_choice=='rock':
            if computer_choice=='paper':
                print('paper can cover rock . Hence ,computer wins.')
            else:
                print('Rock can beat scissor. hence you wins.')

        elif user_choice=='paper':
            if computer_choice=='scissor':
                print('scissor can cut paper hence,computer wins.')
            else:
                print('Paper can cover stone ,hence you wins.')

        elif user_choice=='scissor':
            if computer_choice=='rock':
                print('Rock can beat scissor hence Computer wins.')
            else:
                print('Scissor can cut paper Hence you wins.')
    else:
        print('You have made Invalid choice. Select correct one.')

    play_again=input('Do you want to play again? yes/no :')
    if play_again=='yes':
        continue
    else:
        break
  
        
print('Thanks for playing game.')



