# Task 10: Object-Oriented Programming (OOP)

class BankAccount:
    """
    Base class for bank account
    """

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self._balance = balance  # Encapsulation

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposited {amount}. New balance: {self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient balance")
        else:
            self._balance -= amount
            print(f"Withdrawn {amount}. Remaining balance: {self._balance}")

    def get_balance(self):
        return self._balance


class SavingsAccount(BankAccount):
    """
    Child class demonstrating inheritance and method overriding
    """

    def withdraw(self, amount):
        if amount > self._balance:
            print("Withdrawal denied: Insufficient funds")
        else:
            self._balance -= amount
            print(f"Savings withdrawal: {amount}, Balance: {self._balance}")


# -------- Creating multiple objects --------

account1 = BankAccount("Kapilan", 1000)
account2 = SavingsAccount("Arun", 2000)

# -------- Simulating real bank operations --------

account1.deposit(500)
account1.withdraw(300)

account2.deposit(1000)
account2.withdraw(4000)

print("Final balance (Account 1):", account1.get_balance())
print("Final balance (Account 2):", account2.get_balance())
