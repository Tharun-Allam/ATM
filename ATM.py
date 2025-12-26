import os
from datetime import datetime

class ATM:
    def __init__(self):
        self.pin_file = "pin.txt"
        self.balance_file = "balance.txt"
        self.statement_file = "statement.txt"
        self.pin = self.load_pin()
        self.balance = self.load_balance()


    def load_pin(self):
        if os.path.exists(self.pin_file):
            return int(open(self.pin_file).read())
        return None

    def load_balance(self):
        if os.path.exists(self.balance_file):
            return int(open(self.balance_file).read())
        return 0

    def save_pin(self):
        open(self.pin_file, "w").write(str(self.pin))

    def save_balance(self):
        open(self.balance_file, "w").write(str(self.balance))

    def log_transaction(self, msg):
        with open(self.statement_file, "a") as f:
            f.write(f"{datetime.now()} - {msg}\n")

    def generate_pin(self):
        p = int(input("Enter new 4-digit PIN: "))
        if 1000 <= p <= 9999:
            self.pin = p
            self.save_pin()
            print("PIN generated successfully")
        else:
            print("Invalid PIN")

            
    def verify_pin(self):
        for _ in range(3):
            p = int(input("Enter PIN: "))
            if p == self.pin:
                return True
            print("Incorrect PIN")
        print("Card blocked temporarily")
        return False


    def balance_enquiry(self):
        if self.verify_pin():
            print("Current balance:", self.balance)

    def withdraw(self):
        if self.verify_pin():
            amt = int(input("Enter withdraw amount: "))
            if amt <= self.balance:
                self.balance -= amt
                self.save_balance()
                self.log_transaction(f"Withdrawn: {amt}")
                print("Withdrawal successful")
            else:
                print("Insufficient balance")


    def deposit(self):
        if self.verify_pin():
            amt = int(input("Enter deposit amount: "))
            if amt <= 50000:
                self.balance += amt
                self.save_balance()
                self.log_transaction(f"Deposited: {amt}")
                print("Deposit successful")
            else:
                print("Deposit limit exceeded")


    def mini_statement(self):
        if os.path.exists(self.statement_file):
            print("\nMini Statement:")
            print(open(self.statement_file).read())
        else:
            print("No transactions yet")


    def bank(self):
        while True:
            print("\n=== POCKET BANK ATM ===")
            print("1. Generate PIN")
            print("2. Balance Enquiry")
            print("3. Withdraw")
            print("4. Deposit")
            print("5. Mini Statement")
            print("6. Exit")

            choice = int(input("Enter choice: "))

            match choice:
                case 1: self.generate_pin()
                case 2: self.balance_enquiry()
                case 3: self.withdraw()
                case 4: self.deposit()
                case 5: self.mini_statement()
                case 6:
                    print("Thank you for using Pocket Bank")
                    break
                case _:
                    print("Invalid choice")


atm = ATM()
atm.bank()




    


    