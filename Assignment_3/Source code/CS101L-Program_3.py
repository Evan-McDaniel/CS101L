########################################################################
##
## CS 101 Lab
## Program 3
## Evan McDaniel
## emdby@umsystem.edu
##
## PROBLEM : have user guess a number then have program find out what the number is based on remainders of 3 5 and 7
##
## ALGORITHM : 
##      1. explained on wiki page
## 
## ERROR HANDLING:
##      make sure for the remainder it is a valid number between 0 and up to 1 minus the number
##      check if user enters y or n
## OTHER COMMENTS:
##      Any special comments
##
########################################################################
userval = 'y'
while userval.lower() == 'y':
    print('Welcome to the Flarsheim Guesser!')
    print('Please think of a number between and including 1 and 100.')

    remainder3 = int(input('What is the remainder when your number is divided by 3 ?'))
    while 0>remainder3 or remainder3>2:
        print('The value entered must be greater than or equal to 0 or less than 2')
        remainder3 = int(input('What is the remainder when your number is divided by 3 ?'))
    print()
    remainder5 = int(input('What is the remainder when your number is divided by 5 ?'))
    while 0>remainder5 or remainder5>4:
        print('The value entered must be greater than or equal to 0 or less than 5')
        remainder5 = int(input('What is the remainder when your number is divided by 5 ?'))
    print()
    remainder7 = int(input('What is the remainder when your number is divided by 7 ?'))
    while 0>remainder7 or remainder7>6:
        print('The value entered must be greater than or equal to 0 or less than 7')
        remainder7 = int(input('What is the remainder when your number is divided by 7 ?'))
    print()

    for x in range(0,101):
        print()
        if x%3 == remainder3 and x%5==remainder5 and x%7==remainder7:
            print('Your number was  {}'.format(x))
            print('How amazing is that?')

    list=[]
    for x in range(0,101):
        if x%3 == remainder3:
            list.append(x)
        
    print()

    userval = input('Do you want to play again? Y to continue, N to quit  ==>')
    while userval.lower() != 'y' and userval.lower() != 'n':
        userval = input('Do you want to play again? Y to continue, N to quit  ==>')
        if userval.lower() == 'y':
                break
        elif userval.lower() == 'n':
                 break
        else:
            continue
    if userval.lower() == 'y':
                continue
    elif userval.lower() == 'n':
                 break
  





