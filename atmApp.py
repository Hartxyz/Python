import datetime, random

omniBankDatabase = {} 


def init():
    print("======= WELCOME TO OMNIBANK! ======= \nNOTICE! Open an account with us before 17th April 2020 to receive $2000 free!")
    haveAccount = int(input("Do you have an account with us? \n(1) Yes \n(2) No \n--> "))
    
    if haveAccount == 1:
        login()
    elif haveAccount == 2:
        wantAccount = int(input("Would you like to open an account? \n(1) Yes \n(2) No \n--> "))
        if wantAccount == 1:
            openAccount()
        else: 
            print("Thank you for your time.")
            exit()
    else:
        print("You have selected invalid option")
        init()



def openAccount():
    print("****** OPEN ACCOUNT *******")

    email = input("What is your email address? \n--> ")
    firstName = input("What is your first name? \n--> ")
    lastName = input("What is your last name? \n--> ")
    password = input("Create a 4-digit password for yourself: \n--> ")
    
    accountBalance = 2000
    accountNumber = generateAccountNumber()
    omniBankDatabase[accountNumber] = [ firstName, lastName, email, password, accountBalance ]

    print("Congratulations %s! Your Account has been created and you have received your account opening bonus of $2000!" % firstName)
    print(" == ==== ====== ===== ===")
    print("Your Account Number is: %d and your account balance is $%d" % (accountNumber, accountBalance)) 
    print(" == ==== ====== ===== ===")

    login()


def login():
    print("********* LOGIN ***********")

    accountNumberFromUser = int(input("What is your account number? \n"))
    password = input("What is your password? \n")

    for accountNumber,userDetails in omniBankDatabase.items():
        if(accountNumber == accountNumberFromUser) and (userDetails[3] == password):
            bankOperations(userDetails)
        else:
            print('Invalid account or password')
            login()


def bankOperations(user):
    
    print("======= WELCOME TO OMNIBANK %s %s =======!" % ( user[0], user[1] ) )
    currentDate = datetime.datetime.now()
    print(currentDate)

    selectedOption = int(input("What would you like to do? \n(1) Deposit \n(2) Withdrawal \n(3) Complaints \n(4) Logout \n(5) Exit \n--> "))
    
    if selectedOption == 1:
        
        deposit()
        
    elif selectedOption == 2:
        
        withdrawal()
        
    elif selectedOption == 3:
        
        complaints()
        
    elif selectedOption == 4:
        
        logout()
        
    elif selectedOption == 5:
        exit()
        
    else:
        print("Invalid option selected. Please select another option.")
        bankOperations(user)

def deposit():
    print("======= DEPOSIT =======")
    
    for userDetails in omniBankDatabase.values():
        currentBalance = userDetails[4]
        depositBalance = int(input("How much would you like to deposit? \n-->"))
        currentBalance = currentBalance + depositBalance
        print("Thank you for banking with us. This is your current balance: $%s" %currentBalance)
    
        selectedOption = int(input("Would you like to perform another transaction?\n(1) Yes \n(2) No\n -->"))
        if selectedOption == 1:
            bankOperations(userDetails)
        else:
            logout()
        return currentBalance

def withdrawal():
    print("======= WITHDRAWAL =======")
    for userDetails in omniBankDatabase.values():
        withdrawableBalance = userDetails[4]
        print("This is your withdrawable balance: $%s" %withdrawableBalance)
        requestedFunds = int(input("How much would you like to withdraw? \n"))
        currentBalance = withdrawableBalance - requestedFunds
        if requestedFunds <= withdrawableBalance:
            print("Please take your cash. Your balance is now $%s." %currentBalance)
        else:
            print("You are not that rich. Please try again.")
    
    selectedOption = int(input("Would you like to perform another transaction?\n(1) Yes \n(2) No\n -->"))
    if selectedOption == 1:
        bankOperations(userDetails)
    else:
        logout()
    

def complaints():
    
    print("======= COMPLAINTS =======")
    userComplaint = input("We apologize for any incoveniences caused. Please input your complaint below.\n-->")
    print("Thank you for your time. Expect an email from us soon.")
    
    selectedOption = int(input("Would you like to perform another transaction?\n(1) Yes \n(2) No\n -->"))
    if selectedOption == 1:
        login()
    else:
        logout()
    
    
def logout():
    print("======= LOGOUT =======")
    print("You are now logged out.")

def generateAccountNumber():
        return random.randrange(1111111111,9999999999)

init()