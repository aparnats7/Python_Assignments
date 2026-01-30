class BankAccount:
    ROI = 10.5   # Class variable

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account holder name:", self.Name)
        print("Current balance:", self.Amount)

    def Deposit(self):
        amt = int(input("Enter amount to deposit: "))
        self.Amount = self.Amount + amt
        print("Amount deposited successfully")

    def Withdraw(self):
        amt = int(input("Enter amount to withdraw: "))
        if amt <= self.Amount:
            self.Amount = self.Amount - amt
            print("Withdrawal successful")
        else:
            print("Insufficient balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


def main():
    obj1 = BankAccount("Aparna", 5000)
    obj2 = BankAccount("Rohit", 10000)
    obj3 = BankAccount("Abhishek", 60000)

    print("--- Account 1 ---")
    obj1.Display()
    obj1.Deposit()
    obj1.Withdraw()
    print("Interest:", obj1.CalculateInterest())
    obj1.Display()

    print("--- Account 2 ---")
    obj2.Display()
    obj2.Deposit()
    obj2.Withdraw()
    print("Interest:", obj2.CalculateInterest())
    obj2.Display
    
    print("--- Account 3 ---")
    obj3.Deposit()
    obj3.Display()


if __name__ == "__main__":
    main()