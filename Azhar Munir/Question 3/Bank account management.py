class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("sorry you are out of balance")

    def calculate_interest(self):
        pass

    def deduct_transaction_fee(self):
        pass

    def display_balance(self):
        print(f"Account {self.account_number}: Balance = ${self.balance}")


class SavingsAccount(BankAccount):
    def __init__(self, account_number, balance=0, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * self.interest_rate
        self.deposit(interest)
        print(f"Interest of ${interest} added to account {self.account_number}")

    def display_balance(self):
        super().display_balance()
        print(f"Interest Rate: {self.interest_rate * 100}%")


class CheckingAccount(BankAccount):
    def __init__(self, account_number, balance=0, transaction_fee=1):
        super().__init__(account_number, balance)
        self.transaction_fee = transaction_fee

    def deduct_transaction_fee(self):
        if self.balance >= self.transaction_fee:
            self.balance -= self.transaction_fee
            print(f"Transaction fee of ${self.transaction_fee} deducted from account {self.account_number}")
        else:
            print("Transaction fee can't be deduct due to low balance")

    def display_balance(self):
        super().display_balance()
        print(f"Transaction Fee: ${self.transaction_fee}")

class BankCustomer:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_savings_account(self, account_number, initial_balance=0, interest_rate=0.03):
        savings_account = SavingsAccount(account_number, initial_balance, interest_rate)
        self.accounts[account_number] = savings_account

    def create_checking_account(self, account_number, initial_balance=0, transaction_fee=1):
        checking_account = CheckingAccount(account_number, initial_balance, transaction_fee)
        self.accounts[account_number] = checking_account

    def get_account(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number]
        else:
            print(f"Account {account_number} does not exist for {self.name}")

    def display_accounts(self):
        print(f"Accounts for {self.name}:")
        for account_number, account in self.accounts.items():
            account.display_balance()



if __name__ == "__main__":

    customer = BankCustomer("Azhar")

    customer.create_savings_account(1001, initial_balance=5000)
    customer.create_checking_account(2001, initial_balance=300)


    customer.get_account(1001).deposit(500)
    customer.get_account(2001).withdraw(50)


    customer.display_accounts()

    
    customer.get_account(1001).calculate_interest()
    customer.get_account(2001).deduct_transaction_fee()

   
    customer.display_accounts()
