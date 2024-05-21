# Non OOP
# Bank Version 1
# Single Account

accountName = 'Joe'
accountBalance = 100
accountPassword = 'soup'

while True:
    print('Press b to get the balance')
    print('Press d to make a deposit')
    print('Press w to make a withdrawl')
    print('Press s to show the account')    
    print('Press q to quit')
    
    action = input("What do you want to do? ")
    action = action.lower() #
    action = action[0]
    
    if action == 'b':
        print('Get Balance:')
        userPassword = input('Please enter your password: ')
        if userPassword != accountPassword:
            print('Incorrect Password')
        else:
            print('Your balance is: ', accountBalance)
    elif action == 's':
        print('Show: ')
        print('     Name', accountName)
        print('     Balance', accountBalance)
        print('     Password', accountPassword)
        print()

    elif action == 'q':
        break

    elif action == 'w':
        print('Withdraw: ')

        userWithdrawAmount = input('Please enter your amount: ')

        userWithdrawAmount = int(userWithdrawAmount)
        userPassword = input('Please enter your password: ')

        if userWithdrawAmount < 0:
            print('You cannot withdraw this amount')

        elif userPassword != accountPassword:
            print('Incorrect password')
        
        elif userWithdrawAmount > accountBalance:
            print('Not enough funds')

        else:
            accountBalance = accountBalance - userWithdrawAmount
            print('Your new balance is: ' + str(accountBalance))

    elif action == 'd':
        print('Deposit: ')

        userDepositAmount = input('Please enter your amount: ')

        userDepositAmount = int(userDepositAmount)
        userPassword = input('Please enter your password: ')

        if userDepositAmount < 0:
            print('You cannot deposit this amount')

        elif userPassword != accountPassword:
            print('Incorrect password')

        else:
            accountBalance = accountBalance + userDepositAmount
            print('Your new balance is: ' + str(accountBalance))