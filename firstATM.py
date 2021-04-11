import datetime

name = input("What is your username? \n")
allowedUsers = ['Seyi', 'Favour', 'Kevwe']
allowedPassword = ['2468', '1234', '1359']
totalUserBalance = [10000, 25000, 5000]
bankFee = 1000
currentDate = datetime.datetime.now()


if name in allowedUsers:
    password = (input("Your password? \n"))
    userID = allowedUsers.index(name)
    individualBalance = allowedUsers.index(name)
    if password in allowedPassword[userID]:
        print(currentDate)
        print("Welcome to OmniBank %s." %name)
        print("These are the available options:")
        print("1. Withdrawal")
        print("2. Cash Deposit")
        print("3. Complaint")
        
        selectOption = int(input("Please select an option: \n"))
        
        if selectOption == 1:
            print("You selected %s --> Withdrawal" %selectOption)
            withdrawableBalance = totalUserBalance[individualBalance] - bankFee
            print("This is your withdrawable balance: $%s" %withdrawableBalance)
            requestedFunds = int(input("How much would you like to withdraw? \n"))
            currentBalance = withdrawableBalance - requestedFunds
            if requestedFunds <= withdrawableBalance:
                print("Please take your cash. Your balance is now $%s." %currentBalance)
            else:
                print("You are not that rich. Please try again.")
        
        elif selectOption == 2:
            print("You selected %s --> Deposit" %selectOption)
            depositBalance = int(input("How much would you like to deposit? \nNOTICE: Maximum deposit is $100,000 \n"))
            currentBalance = totalUserBalance[individualBalance] + depositBalance
            if depositBalance > 100000:
                print("Deposit limit exceeded. Invalid transaction.")
            else:
                print("Thank you for banking with us. This is your current balance: $%s" %currentBalance)
        
        elif selectOption == 3:
            print("You selected %s --> Complaint" %selectOption)
            issue = input("What issue will you like to report? \n")
            print("Thank you for contacting us.")
        
        else: 
            print("Invalid option selected, please try again.")
    
    else:
        print("Password incorrect, please try again.")

else: 
    print("Name not found, please try again.")