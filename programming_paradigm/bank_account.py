class BankAccount:
    def __init__(self, account_balance):
        self.account_balance = account_balance
        account_balance = 100

    def deposit(self, amount):
        result = amount + self.account_balance
        return result

    def withdraw(self, amount):
        result = amount - self.account_balance
        if amount < self.account_balance:
            return True
        else:
            return False

    def display_balance(self):
        self.account_balance = result
        print(f"Current Balance: {self.account_balance}")
