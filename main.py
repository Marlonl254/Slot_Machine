'''
This is my main file where my logic is written
'''

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

