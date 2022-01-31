
import random

account = {}

def init():

    isValidOptionSelected = False
    print("welcome to access bank")

    while isValidOptionSelected == False:

        haveAccount = int(input("do you have an account with us: 1(yes) 2 (no) \n"))
        
        if (haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else: 
            print("you have selected an invalid option")


def login():
    print("this is a login function")

def  register():
    print("this is a register function")

def bankOperation():
    print("some operation")

def accountNumber():

    print("account number generator")
    return random.randrange(1111111111,9999999999)

print(accountNumber())



# def accountNumber():
# return random.randrange(1111111111,999999999)

# print(accountNumber)

