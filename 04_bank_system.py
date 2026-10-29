class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.history = []
    
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive!")
        self.balance = self.balance + amount
        record = f"DEPOSIT: +{amount} | Balance: {self.balance}"
        self.history.append(record)
        print(f"Deposited {amount}. New balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance = self.balance - amount
        record = f"WITHDRAW: -{amount} | Balance: {self.balance}"
        self.history.append(record)
        print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def show_history(self):
        if len(self.history) == 0:
            print("No transactions yet!")
        else:
            for record in self.history:
                print(record)
    
    def save_history(self, filename):
        file = open(filename, "w")
        for record in self.history:
            file.write(record + "\n")
        file.close()
        print(f"History saved to {filename}")
    
    def __str__(self):
        return f"{self.owner}: {self.balance}"


class SavingsAccount(Account):
    def __init__(self, owner, balance=0, interest_rate=0.05):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate
    
    def add_interest(self):
        interest = self.balance * self.interest_rate
        self.balance = self.balance + interest
        record = f"INTEREST: +{interest} | Balance: {self.balance}"
        self.history.append(record)
        print(f"Interest added: {interest}. New balance: {self.balance}")
    
    def __str__(self):
        return f"SavingsAccount({self.owner}): {self.balance}"


class CheckingAccount(Account):
    def __init__(self, owner, balance=0, overdraft_limit=100):
        super().__init__(owner, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")
        if amount > self.balance + self.overdraft_limit:
            raise ValueError("Exceeds overdraft limit!")
        self.balance = self.balance - amount
        record = f"WITHDRAW: -{amount} | Balance: {self.balance}"
        self.history.append(record)
        print(f"Withdrew {amount}. New balance: {self.balance}")
    
    def __str__(self):
        return f"CheckingAccount({self.owner}): {self.balance}"


# Main program
savings = SavingsAccount("Arash", 1000)
checking = CheckingAccount("Kourosh", 500)

accounts = [savings, checking]

while True:
    print("\n--- BANKING SYSTEM ---")
    print("1. Show Accounts")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Show History")
    print("5. Save History")
    print("6. Add Interest (Savings)")
    print("q. Quit")
    
    choice = input("Choose: ")
    
    if choice == "q":
        print("Goodbye!")
        break
    
    if choice == "1":
        for acc in accounts:
            print(acc)
    
    elif choice in ["2", "3", "4", "5", "6"]:
        print("Choose account:")
        for i in range(len(accounts)):
            print(f"{i + 1}. {accounts[i].owner}")
        
        try:
            acc_index = int(input("Account number: ")) - 1
            if acc_index < 0 or acc_index >= len(accounts):
                print("Invalid account!")
                continue
            account = accounts[acc_index]
        except ValueError:
            print("Please enter a number!")
            continue
        
        try:
            if choice == "2":
                amount = float(input("Deposit amount: "))
                account.deposit(amount)
            elif choice == "3":
                amount = float(input("Withdraw amount: "))
                account.withdraw(amount)
            elif choice == "4":
                account.show_history()
            elif choice == "5":
                filename = input("Filename: ")
                account.save_history(filename)
            elif choice == "6":
                if isinstance(account, SavingsAccount):
                    account.add_interest()
                else:
                    print("Only for Savings accounts!")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Invalid choice!")