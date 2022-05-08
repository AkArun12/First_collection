#Python program to find Treasure.
print(':::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
print("welcome to Treasure island.\nYour mission is to find the treasure. ")
print('----------------------------------------------------------------------')
'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/////////
*******************************************************************************

'''


while True:
    print('Game starts from here.....')
    direction=input('Which way do you want to go :left or right ? :')
    if direction=='left':
        second_step=input('congrats you have crossed 1st step. Do you want to swim or wait now? :')
        if second_step=='wait':
            print('wow , You reached level second.')
            third_step=input('which door do you want to select: Red, Blue or Yellow :' )
            if third_step=='yellow':
                print('Huge congratulations , You found the treasure and won the game.')
            else:
                print('oops you lose. GAme Over !!!')
        else:
            print('GAme Over')


    else:
        print('Opps you lose the game. Game Over!!!!')
    
    play_again=input('Do you want to play again? yes/no :')
    if play_again=='yes':
        continue
    else:
        break

print('Thanks for playing.')
    


