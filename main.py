from classes.bank_account import BankAccount

if __name__ == "__main__":
    account1 = BankAccount("Ari durlacher", 10000)
    account2 = BankAccount("meir",10000)

    account1.__str__()
    account2.__str__()

    transfer_money = account1.transfer_funds(account2,5000)

    account1.__str__()
    account2.__str__()