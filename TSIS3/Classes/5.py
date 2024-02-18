class Account:
    def __init__(self, owner, balance=0
                 ):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):

        print("Balance:", self.balance)
        if amount >= 0:
            self.balance += amount
            print("Balance:", self.balance)
        else:
            print("Invalid input")

    def withdraw(self, amount):
        
        print("Balance:", self.balance)
        
        if 0 <= amount <= self.balance:
            self.balance-=amount
            print("Withdrawal:", amount)
            print("Balance:", self.balance)
        else:
            print("You don't have so much")


owner = input("Enter account owner's name: ")
account = Account(owner)
print(f"Account owner: {account.owner}")

while True:
    choice = input("Enter 'D' to deposit, 'W' to withdraw, or 'Q' to quit: ").upper()
    if choice == 'Q':
        break
    elif choice == 'D':
        amount = float(input("Enter deposit amount: "))
        account.deposit(amount)
    elif choice == 'W':
        amount = float(input("Enter withdrawal amount: "))
        account.withdraw(amount)
    else:
        print("Invalid choice.")