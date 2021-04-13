# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# Initialising the system
import random

database = {}

def init():

        print('welcome to our bank')

        haveAcount = int(input('do you have account with us: 1 (yes) 2 (No) \n'))
        if(haveAcount == 1):
          login()
        elif(haveAcount == 2):
          register()
        else:
          print('You have selected invalid option')
        init()

def login():
    print('***** Login *****')



    accountNumberFromUser = int(input('What is your account number? \n'))
    password = input('What is your password? \n')

    for accountNumber,userDetails in database.items():
      if(accountNumber == accountNumberFromUser):
       if(userDetails[3] == password):
        bankOPeration(userDetails)

    print('invalid account or password')
    init() # returns you back to the beginnings



def register():

    print('****** Register ******')

    Email = input('What is your Email? \n')
    Last_Name = input('What is your LastName? \n')
    First_Name = input('What is your FirstName? \n')
    password = input('Create Password for yourself? \n')

    accountNumber = generateAcountNumble()

    database[accountNumber] = [ Last_Name , First_Name, Email,password ]

    print('Your account has been Created')
    print('= === ==== ======')
    print('Your account number is: %d ' %accountNumber )
    print('Make sure you keep it safe')
    print('== === ==== =====')

    login()

def bankOPeration(user):
    print('Welcome %s %s' % (user[0], user[1] ))

    selectedoptions = int(input(' What would you like to do? (1) Withhdrawer (2).deposite (3).login (4). exit \n'))
    if(selectedoptions == 1):
        Withdraweroperation()
    elif(selectedoptions == 2):
        depositeoperation()
    elif(selectedoptions == 3):
        login()
    elif(selectedoptions == 4):
        exit()
    else:
        print('Invalid option selected')
        bankOPeration()

def  Withdraweroperation():
    print('Withdrawer')

def depositeoperation():
    print('Deposite')


def generateAcountNumble():

    return random.randrange(1111111111.9999999999) # these how to generate account number with import ramdom


    ### Actual Banking System ##
init()
