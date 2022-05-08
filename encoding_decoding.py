#Python code to encode and decode letters/words.
import string
a=list(string.ascii_lowercase)
#ascii gives us the alphabets from a to z.
alphabet=2*a
while True:
    direction=input("Type 'encode' to Encode, type 'decode' to to Decode :")
    direction_choice=['encode','decode']
    if direction in direction_choice:
        text=input('Enter the text :')
        shift=int(input('Enter the shift number :'))
    
        def encrypt(text_new,shift_num):
            if direction=='encode':
                encoded_text=''
                for letter in text:
                    position=alphabet.index(letter)
                    new_position=position+shift_num
                    new_letter=alphabet[new_position]
                    encoded_text+=new_letter
                print(f'The encoded text is {encoded_text}')

            else:
                decoded_text=''
                for letter in text:
                    position=alphabet.index(letter)
                    new_position=position-shift_num
                    new_letter=alphabet[new_position]
                    decoded_text+=new_letter
                print(f'The decoded text is {decoded_text}')
                

        encrypt(text_new=text,shift_num=shift)
        check_again=input('Do you want to check again (yes/no):')
        if check_again=='yes':
            continue
        else:
            print('Thanks for using our App.')
            break
    else:
        print('Invalid choice. Please choose either encode or decode :')   