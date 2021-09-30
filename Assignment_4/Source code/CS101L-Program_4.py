
########################################################################
##
## CS 101 Lab
## Program 4
## Evan McDaniel
## Emdby@umsystem.edu
##
## PROBLEM : Create a slot machine program to spin 3 reels and adds a payout to the users 
#            bank account depending on how many matches they got then ask user to play again
##
## ALGORITHM : 
##      1. create functions for play_again, get_wager, get_slot_results, get_matches, get_bank, get_payout
##      2. set up a loop for program to run while player wants to play again
##      3. call get_bank function to have user input bank amount
##      4. set loop to run while bank is greater than 0
##      5. have user input wager and have program get slot values, then update payout and bank values
##      6. print out the reels, matches, payout and bank values
##      7. once bank is 0 exit loop, tell the user they lost, then ask if they want to play again
## 
## ERROR HANDLING:
##      check if user enters a bank value between 1 and 100, 
#       check if their wager is between 0 and their bank account value
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################

#import modules needed
import random 


def play_again() -> bool:
    ''' Asks the user if they want to play again, returns False if N or NO, and True if Y or YES.  Keeps asking until they respond yes '''
    user_input = input('Would you like to play again:\n').upper()
    while True:
        if user_input == 'Y' or user_input == 'YES':
            return True
        elif user_input == 'N' or user_input == 'NO':
            return False
        else:
            user_input = input('Please enter a valid value:\n').upper()
     
def get_wager(bank : int) -> int:
    ''' Asks the user for a wager chip amount.  Continues to ask if they result is <= 0 or greater than the amount they have '''
    user_input = int(input('Enter wager amount:\n'))
    while user_input<=0 or user_input>bank:
        user_input = int(input('Enter a valid value:\n'))
    return user_input

def get_slot_results() -> tuple:
    ''' Returns the result of the slot pull '''
    slot1 = random.randint(1,10)
    slot2 = random.randint(1,10)
    slot3 = random.randint(1,10)
    return slot1, slot2, slot3

def get_matches(reela, reelb, reelc) -> int:
    ''' Returns 3 for all 3 match, 2 for 2 alike, and 0 for none alike. '''
    if reela == reelb == reelc:
        return 3
    elif reela != reelb and reela != reelc and reelb != reelc:
        return 0
    else:
        return 2


def get_bank() -> int:
    ''' Returns how many chips the user wants to play with.  Loops until a value greater than 0 and less than 101 '''
    user_input = int(input('How many chips do you want to play with? : \n'))
    while user_input <= 0 or user_input >100:
        user_input = int(input('Enter an amount between 1 and 100:\n'))
    return user_input

def get_payout(wager, matches):
    ''' Returns how much the payout is.. 10 times the wager if 3 matched, 3 times the wager if 2 match, and negative wager if 0 match '''
    if matches == 3:
        return wager*10-wager
    elif matches == 2:
        return wager*3-wager
    else:
        return -wager
    return wager * -1     


if __name__ == "__main__":

    playing = True
    while playing:

        bank = get_bank()
        bank1 = bank
        counter = 0
        max = bank

        while bank > 0:  # Replace with condition for if they still have money.
            
            wager = get_wager(bank)

            reel1, reel2, reel3 = get_slot_results()

            matches = get_matches(reel1, reel2, reel3)
            payout = get_payout(wager, matches)
            bank = bank + payout

            print("Your spin", reel1, reel2, reel3)
            print("You matched", matches, "reels")
            print("You won/lost", payout)
            print("Current bank", bank)
            print()
            counter += 1
            if bank > max:
                max = bank
           
        print("You lost all", bank1, "in", counter, "spins")
        print("The most chips you had was", max)
        playing = play_again()
