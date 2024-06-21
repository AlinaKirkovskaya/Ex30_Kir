class Logger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Logger, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'logs'):
            self.logs = []

    def log(self, message):
        self.logs.append(message)
        print(message)  # Для простоти будемо також виводити лог на екран

    def get_logs(self):
        return self.logs


class BankAccount:
    def __init__(self, accountNumber, initial_balance=0):
        self.accountNumber = accountNumber
        self.balance = initial_balance
        self.logger = Logger()
        self.logger.log(f"Account {self.accountNumber} created with balance {self.balance}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.logger.log(f"Deposited {amount} to account {self.accountNumber}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self.balance:
            self.logger.log(f"Attempt to withdraw {amount} from account {self.accountNumber} failed due to insufficient funds")
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.logger.log(f"Withdrew {amount} from account {self.accountNumber}. New balance: {self.balance}")

# Тестування функціональності
if __name__ == "__main__":
    # Створення облікового запису
    account = BankAccount("123456", 1000)

    # Внесення коштів
    account.deposit(500)

    # Спроба зняття коштів
    try:
        account.withdraw(200)
    except ValueError as e:
        print(e)

    # Спроба зняття коштів з недостатнім балансом
    try:
        account.withdraw(2000)
    except ValueError as e:
        print(e)

    # Перевірка логів
    logger = Logger()
    for log in logger.get_logs():
        print(log)