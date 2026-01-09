import random

class BankAccount:
    accounts : dict[str, 'BankAccount'] = {}

    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.account_number = BankAccount.generate_account_number()
        self._balance = 0.0

        BankAccount.accounts[self.account_number] = self
        print(f"Account created for {self.owner} with account number {self.account_number}")

    @property
    def balance(self) -> float:
        return self._balance

    @balance.setter
    def balance(self, balance: float) -> None:
        self._balance = balance

    @classmethod
    def generate_account_number(cls) -> str:
        account_number = str(random.randint(100000, 999999))
        if account_number in cls.accounts:
            account_number = cls.generate_account_number()
        return account_number

    @staticmethod
    def is_valid_amount(amount: float) -> bool:
        return amount > 0

    def deposit(self, amount: float) -> None:
        if not BankAccount.is_valid_amount(amount=amount):
            print("\t#### Invalid deposit amount ###")
            return
        self._balance += amount

    def withdraw(self, amount: float) -> None:
        if not BankAccount.is_valid_amount(amount=amount):
            print("\t#### Invalid withdrawal amount ###")
            return
        
        if amount > self._balance:
            print("\t#### Insufficient funds ###")
            return

        self._balance -= amount

    def show_balance(self) -> None:
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

    @classmethod
    def total_accounts(cls) -> int:
        return len(cls.accounts)

    @classmethod
    def get_account(cls, account_number: str) -> 'BankAccount':
        return cls.accounts.get(account_number)