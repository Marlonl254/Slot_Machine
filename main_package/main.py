'''
This is my main file where my logic is written
'''

LINES = 3


def deposit():
    '''Used to set the ammount of money in the users account'''
    while True:
        ammount = input("Enter ammount of money to deposit in (ksh): ")
        if ammount.isdigit():
            ammount = int(ammount)
            print(f"You have successfully deposited {ammount} ksh")
            break
        else:
            raise ValueError("Invalid input (must be a digit)")
    return ammount


def get_number_of_lines():
    '''Gets the number of lines the userr wants to bet on'''
    while True:
        number = input("How many lines do you want to bet on? (1 - 3): ")
        if number.isdigit():
            number = int(number)
            if 0 < number <= LINES: # Checks if number is greater than zero and less than or equal to three
                break
            else:
                print("Bet between 1 and 3 lines")
        else:
            raise ValueError("Enter a valid number between 1 - 3")
    return number

