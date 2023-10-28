class SavingsAccount:
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.02

class CurrentAccount:
    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self):
        return self.balance * 0.01

# Usage
savings_account = SavingsAccount(5000)
current_account = CurrentAccount(3000)

print("Interest earned in savings account:", savings_account.calculate_interest())
print("Interest earned in current account:", current_account.calculate_interest())

"""
In this code, we have two account classes, SavingsAccount and CurrentAccount, 
each with its own calculate_interest method. If you wanted to add more account 
types like "FixedDepositAccount" or "InvestmentAccount," you would need to 
modify these classes and their methods, violating the Open-Closed Principle.

Now, let's refactor this code to adhere to the Open-Closed Principle:
"""

from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def calculate_interest(self):
        pass

class SavingsAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.02

class CurrentAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.01

class FixedDepositAccount(Account):
    def calculate_interest(self):
        return self.balance * 0.03

# Usage
savings_account = SavingsAccount(5000)
current_account = CurrentAccount(3000)
fixed_deposit_account = FixedDepositAccount(10000)

accounts = [savings_account, current_account, fixed_deposit_account]

for account in accounts:
    print(f"Interest earned in {account.__class__.__name__}: {account.calculate_interest()}")
