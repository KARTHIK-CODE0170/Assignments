from bank import BankAccount
def main():
    b1 = BankAccount("Ravi Kumar","Savings",5000,1234)
    b2 = BankAccount("Dileep","Current",20000,1111)
    print(BankAccount.BANK_NAME)
    print(b1)
    print(b2)
    print("Total accounts : ",BankAccount.total_accounts)
    print("Deposit 2000 ->",b1.deposit(2000))
    print("Withdraw 1500 ->",b1.withdraw(1500,1234))
    print("Intrest added ->",b1.add_annual_interest())
    print("Balance now : ",b1.balance)
    b1.change_pin(1234,1235)
    b1.withdraw(123,4)
    b1.withdraw(555555,1235)
    b1.deposit(-1)
    b1.balance = 100

    
if __name__ == "__main__":
    main()
