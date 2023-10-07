class Banking:
    def __init__(self, amount):
        self.amount = amount
        print(f"\nWelcome to Bank Account!\nCurrently you have {amount}$ in your balance")
        transaction_file = open("transactions.txt","w")
        transaction_file.write(f"Your current balance is {amount}$\n")
        transaction_file.close()
    
    def current_amount(self):
        print(f"Your current balance is {self.amount}$")
    
    def deposit(self, deposit):
        if deposit >= 0:
            transaction_file = open("transactions.txt","a")
            transaction_file.write(f"+{deposit}$")
            self.amount += deposit
            transaction_file.write(f"\t = {self.amount}$\n")
            transaction_file.close()
            print(f"\nYou have {self.amount}$ on your balance now")
            
        else:
            print("Deposit amount cannot be less than 0$")

    def withdraw(self, withdraw):
        if withdraw >= 0:
            if withdraw <= self.amount:
                transaction_file = open("transactions.txt","a")
                transaction_file.write(f"-{withdraw}$")
                self.amount -= withdraw
                transaction_file.write(f"\t = {self.amount}$\n")
                transaction_file.close()
                print(f"\nYou have {self.amount}$ on your balance now")
            else: 
                print("Insufficient funds. Withdrawal canceled.")
        else:
            print("Withdraw amount cannot be less than 0$")

class MyBank(Banking):
    def __init__(self, amount):
        super().__init__(amount)
        

acc = MyBank(1000)

while True:
    try:
        action = int(input("\nPlease enter number of action you want to execute (1. Deposit Money; 2. Withdraw Money; 3. Exit): "))
        if action not in [1, 2, 3]:
            print("Please use number 1, 2 or 3 only!")
            continue
    except Exception:
        print (f"Unknown value, please use number 1, 2 or 3 only!")
        continue

    if action == 1: 
        try:
            deposit = int(input("\nEnter how much you want to deposit: "))
        except ValueError:
            print(f"Invalid input for deposit amount, please use numbers only!")
            continue

        acc.deposit(deposit)
    elif action == 2:
        try:
            withdraw = int(input("\nEnter how much you want to withdraw: "))
        except ValueError :
            print(f"Invalid input for withdraw amount, please use numbers only!")
            continue

        acc.withdraw(withdraw)
    
    elif action == 3:
        print("\nThank you for using our Banking System\nAll transactions saved in a 'transactions.txt' text file.\nBye!")
        transaction_file = open("transactions.txt","a")
        transaction_file.write(f"Transactions done!")
        transaction_file.close()
        break

    else:
        continue
        