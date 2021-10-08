########################################################################
##
## CS 101 Lab
## Program 5
## Evan McDaniel
## emdby@umsystem.edu
##
## PROBLEM : Create a program that prompts for a user library card and then states if it is valid or not and the 
# reason why if it is invlaid. it calculates a check digit and lets the user know if the card is correct
##
## ALGORITHM : 
##      1. Write functions to get character value of char, check digit, school, grade, and verify check digit to verify if valid
##      2. have program ask the user for a card number
##      3. program run calculations to verfiy values and check digit and print to user if card is valid or not
## 
## ERROR HANDLING:
##      check if user card values are correct(0-4 = letter, 5-9 = number, if 9 is correct calculated check digit)
##
## OTHER COMMENTS:
##      Any special comments
########################################################################
import string
def character_value(char : str) -> int:
    ''' Returns 0 for A, 1 for B, etc. '''
    if char.isalpha():
        return string.ascii_uppercase.index(char)
    elif char.isnumeric():
        return int(char)
    
def get_check_digit(libcard : str) -> int:
    ''' Returns the check digit for the name and sid. '''
    check = libcard[9]
    letters = libcard[0:5]
    numbers = []
    for x in letters:
        a = string.ascii_uppercase.index(x)
        numbers.append(a)
    for x in libcard[5:10]:
        numbers.append(character_value(x))
    sum = 0
    for x in range(len(numbers)):
        sum += (x+1)*(numbers[x])
    return sum%10

def is_valid(libcard : str) -> tuple:
    ''' returns 2 values bool and a string with errors if bool is False '''
    pass

def verify_check_digit(libcard : str) -> tuple:
    ''' returns True if the check digit is valid, False if not '''
    if len(libcard) != 10:
        return (False, "The length of the number given must be 10")
    elif libcard[0:5].isalpha() == False:
        for x in libcard[0:5]:
            if x.isalpha() != True:
                index = libcard.find(x)
                val = x
        return (False, 'The first 5 characters must be A-Z, the invalid character is at {} is {}'.format(index,val))
    elif libcard[7:10].isnumeric() != True:
        for x in libcard[7:10]:
            if character_value(x) not in range(0,10) or x.isalpha():
                val = x
                num = libcard[7:10].find(x)+7
        return(False, 'The last 3 characters must be 0-9, the invalid character is at {} is {}'.format(num,val))
    elif libcard[5] not in ['1','2','3']:
        return(False, "The sixth character must be 1 2 or 3")
    elif libcard[6] not in ['1','2','3','4']:
        return(False, "The seventh character must be 1 2 3 or 4")
    elif int(libcard[9]) != get_check_digit(libcard) or libcard[9].isalpha():
        return (False, "Check Digit {} does not match calculated value {}.".format(libcard[9],get_check_digit(libcard)))
    else:
        return True,''

def get_school(libcard : str) -> str:
    ''' Returns the school the 5th index or 6th character is for. '''
    num = int(libcard[5])
    if num == 1:
        return 'School of Computing and Engineering SCE'
    if num == 2:
        return 'School of Law'
    if num == 3:
        return 'College of Arts and Sciences'
    else:
        return 'Invalid School'
  
def get_grade(libcard : str) -> str:
   '''Returns the grade for index 6'''
   num = int(libcard[6])
   grade = {1:'Freshman', 2:'Sophomore',3:'Junior',4:'Senior',5:'Invalid Grade'}
   return grade[num]
   
if __name__ == "__main__":

    print("{:^60}".format("Linda Hall"))
    print("{:^60}".format("Library Card Check"))
    print("="*60)

    while True:
        print()
        card_num = input("Enter Libary Card. Hit Enter to Exit ==> ").upper().strip()
        if card_num == "":
            break
        result, error = verify_check_digit(card_num)
        if result == True:
            print("Library card is valid.")
            print("The card belongs to a student in {}".format(get_school(card_num)))
            print("The card belongs to a {}".format(get_grade(card_num)))
        else:
            print("Libary card is invalid.")
            print(error)
        