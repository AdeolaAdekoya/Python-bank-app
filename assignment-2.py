
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
            print(register())
        else: 
            print("you have selected an invalid option")


def login():
    print("login to your account")


def  register():
    print("Register your account")
    email = input("input your email address \n ")
    First_name = input ("input your first name \n")
    last_name = input ("input your last name \n")
    user_name = input ("input your user name \n")
    password = input ("Create Password \n")


    accountNum = accountNumber()

    account[accountNum] = [ First_name, last_name, user_name, email, password]

    print("you have sucessfully created an account")


    login()

def withdrawl():
    print("withdrawal")



def accountNumber():
    return random.randrange(1111111111,9999999999)



init()

# def accountNumber():
# return random.randrange(1111111111,999999999)

# print(accountNumber)

