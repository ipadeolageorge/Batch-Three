'''import random
generated_number= random.randint(1,100)
print (generated_number)
while True:
    guessed_number=int(input('input your number please: '))
    if guessed_number==generated_number:
        print (guessed_number, 'is correct')
        break
    elif guessed_number>generated_number:
        print(guessed_number, 'is too much')
    else:
        guessed_number<generated_number
        print(guessed_number, 'is too small')
import random
while True:
    generated_number= random.randint(1,100)
    print (generated_number)
    while True:
        guessed_number=int(input('input your number please: '))
        if guessed_number==generated_number:
            print (guessed_number, 'is correct')
            print ('PLEASE GUESS NEXT NUMBER')
            break
        elif guessed_number>generated_number:
            print(guessed_number, 'is too much')
        else:
            guessed_number<generated_number
            print(guessed_number, 'is too small')


    print('Instruction\n A number would be generated by your computer\n and you are to guess what number it is\n Your guess should be between 0 and 100\n Good Luck')
    guessed_number=0
    import random
    while True:
        generated_number= random.randint(1,100)
        print (generated_number)
        while guessed_number<3:
            guessed_number=int(input('input number please: '))
            if guessed_number==generated_number:
                print (guessed_number, 'is correct')
                print ('CONGRATULATIONS\n PLEASE GUESS ANOTHER NUMBER')
                break
            elif guessed_number>generated_number:
                print(guessed_number, 'is too much')
            else:
                guessed_number<generated_number
                print(guessed_number, 'is too small')
                guessed_number=guessed_number+1
                if guessed_number ==3:
                    break



def guess_number_game ():
    print('Instruction\n A number would be generated by your computer\n and you are to guess what number it is\n Your guess should be between 0 and 100\n You have 3 chances\n Good Luck!!!')
    count=0
    import random
    if count <3:
        generated_number= random.randint(1,100)
        print (generated_number)
        while count<3:
            guessed_number=int(input('input number please: '))
            count=count+1
            if count==3:
                print('You are out!!!')
                break
            if guessed_number==generated_number:
                print (guessed_number, 'is correct')
                print ('CONGRATULATIONS\n YOU CAN GO TO THE NEXT LEVEL')
                break
            elif guessed_number>generated_number:
                print(guessed_number, 'is too much')
            else:
                guessed_number<generated_number
                print(guessed_number, 'is too small')

                
guess_number_game()

'''

def guess_number_game ():
    print('Instruction\n A number would be generated by your computer\n and you are to guess what number it is\n Your guess should be between 0 and 100\n You have 7 chances\n Good Luck!!!')
    print(' ')
    count=0
    import random
    if count <7:
        generated_number= random.randint(1,100)
        print (generated_number)
        while count<7:
            guessed_number=int(input('guess the mistery number: '))
            print('you have ',str(6-count) ,'guesses more')
            if guessed_number==generated_number:
                print (guessed_number, 'is correct')
                print ('CONGRATULATIONS\n YOU CAN GO TO THE NEXT LEVEL')
                break
            elif guessed_number>generated_number:
                print(guessed_number, 'is too much')
            else:
                guessed_number<generated_number
                print(guessed_number, 'is too small')
            if (guessed_number-generated_number)<2 and (generated_number-guessed_number<2):
                print('though you are very close')
                print(' ')
            else:
                print('and its not close at all')
                print(' ')
            count=count+1
            if count==7:
                print('the mistery number is ',generated_number)
                print('You are out!!!\n GAME OVER')
                break

                
guess_number_game()

