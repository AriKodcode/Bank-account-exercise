class BankAccount:

    def __init__(self,account_holder : str,initial_balance : float):
        self.account_holder = account_holder
        self.initial_balance = initial_balance

    def transfer_funds(self, other_account, amount):
        if self.initial_balance >= amount:
            self.initial_balance -= amount
            other_account.initial_balance += amount
            print("Transfer completed successfully.")
        else:
            print("There is not enough money to transfer")

    def __str__(self):
       print (f"account status:\naccount holder: {self.account_holder}\nbalance: {self.initial_balance}")






