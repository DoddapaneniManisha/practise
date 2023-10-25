class BankAccount:
    def __init__(self, balance=0):
        self._balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    def get_balance(self):
        return self._balance

# Creating a BankAccount object
account = BankAccount()

account.deposit(1000)
account.withdraw(500)
print(f"Current balance: {account.get_balance()}")
