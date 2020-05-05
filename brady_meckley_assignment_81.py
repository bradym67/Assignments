#Change
class BankAccount:
    def __init__(self, accountNumber, balance):
        self.accountNumber = accountNumber
        self.balance = balance

    def withdrawBalance(self, withdraw):
        self.balance -= withdraw
        return self.balance

    def depositBalance(self, deposit):
        self.balance += deposit
        return self.balance

    def getBalance(self):
        print(f'Your account has ${self.balance}.')
        return self.balance


class CheckingAccount(BankAccount):
    def __init__(self, accountNumber, balance, fees, minimumbalance):
        super().__init__(accountNumber, balance)
        self.fees = fees
        self.minimumbalance = minimumbalance

    def deductFees(self):
        self.balance -= self.fees
        return self.balance
    
    def checkMinimumBalance(self):
        if self.balance < self.minimumbalance:
            print(f'Your account has ${self.balance}. The minimum required balance is $50. '
            'Please add funds soon.')
        else:
            print(f"Your account has ${self.balance}.")

class SavingsAccount(BankAccount):
    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate
    def addInterest(self):
        self.balance *= self.interestRate
        return self.balance


ValidInput = True
while ValidInput:
    try:
        access = input("\nWhich account would you like to access? Enter 'q' to quit (Checking "
        "Account or Savings Account): ")
        if access == 'q':
            break
    

        if access == 'Checking Account':
            accountNumber = input("Please enter your account number: ")
            accountNumber = int(accountNumber)
            balance = input("Please enter your monthly balance: ")
            balance = int(balance)
            my_bank_account = CheckingAccount(accountNumber, balance, 5, 50)
            my_bank_account.checkMinimumBalance()
           
            try:
                action = input("\nWould you like to make a deposit, withdrawal or check the balance "
                "? Enter 'q' to quit. (Enter 'deposit', 'withdrawal' or 'check': ")
                if action == 'q':
                    break
            except:
                print('Invalid input. Please Try again.')
           
            if action == 'deposit':
                deposit = input('How much would you like to deposit?')
                deposit = int(deposit)
                my_bank_account.depositBalance(deposit)
                my_bank_account.deductFees()
                print(my_bank_account.checkMinimumBalance())
           
            if action == 'withdrawal':
                withdrawal = input("How much would you like to withdrawal?")
                withdrawal = int(withdrawal)
                my_bank_account.withdrawBalance(withdrawal)
                my_bank_account.deductFees()
                print(f"{my_bank_account.checkMinimumBalance()}$5 fee has been applied.")
           
            if action == 'check':
                print(my_bank_account.checkMinimumBalance())
        
       
        if access == 'Savings Account':
            accountNumber = input("Please enter your account number: ")
            accountNumber = int(accountNumber)
            balance = input("Please enter your monthly balance: ")
            balance = int(balance)
            my_bank_account = SavingsAccount(accountNumber, balance, 1.02)
            print(f"Your savings's account balance after the monthly interest rate is ${my_bank_account.addInterest()}")
    except:
        print("Invalid input. Please enter 'Checking Account' or 'Savings Account'.")