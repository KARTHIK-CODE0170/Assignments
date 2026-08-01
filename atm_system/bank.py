class BankAccount:
    _next_account_number = 1001
    BANK_NAME = "State Bank of India"
    total_accounts = 0
    MIN_BALANCE = 500   
    INTREST_RATE = 4.0
    def __init__(self,holder_name='',account_type='Savings',balance=0,pin=0):

        self.name = holder_name
        if balance < BankAccount.MIN_BALANCE:
            raise ValueError(f"Balance is not more than {BankAccount.MIN_BALANCE}")
        self.__balance = balance
        self._account_number = BankAccount._next_account_number
        self._account_type = account_type
        if len(str(pin)) == 4:
            self.__pin = pin
        else:
            raise ValueError("Pin must be 4 digits")
        BankAccount._next_account_number += 1
        BankAccount.total_accounts += 1

    def __verify_pin(self,pin):
        if self.__pin == pin:
            return True
        else:
            return False


    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self,val):
        try:
            raise AttributeError("Blocked (write balance): property 'balance' of 'BankAccount' object has no setter")
        except Exception as e:
            print(e)

    @property
    def account_type(self):
        return self._account_type

    @staticmethod
    def next_account_number():
        print(BankAccount._next_account_number)
    
    @property
    def account(self):
        return self.__balance
    @account.setter
    def account(self,amount):
        try:
            raise AttributeError("Blocked (write balance): property 'balance' of 'BankAccount' object has no setter")
        except AttributeError as e:
            print(e)

    @property
    def account_number(self):
        return self._account_number

    def deposit(self,amount):
        try:
            if amount < 0:
                raise ValueError("Blocked (negative): Deposit amount must be positive")
            else:
                self.__balance += amount
                return self.__balance
        except Exception as e:
            print(f"Error : {e}")

    def withdraw(self, amount, pin):
        try:
            if self.__verify_pin(pin):
                if self.__balance - amount < 500:
                    raise ValueError("Blocked (below min): Insufficient funds. Minimum balance 500 must remain")
                else:
                    print(f"With-drawl amount is {amount}")
                    self.__balance -= amount
                    return self.__balance
            else:
                raise ValueError("Blocked (wrong PIN): Incorrect PIN")
        except Exception as e:
            print(f"Error : {e}")
#PIN
    def change_pin(self,curr_pin,new_pin):
        try:
            if self.__verify_pin(curr_pin):
                if len(str(new_pin)) == 4:
                    self.__pin = new_pin
                    print("Pin changed sucessfully")
                else:
                    raise ValueError("Pin must be 4 digits")
            else:
                raise ValueError("Blocked (wrong PIN): Incorrect PIN")
        except Exception as e:
            print(f"Error : {e}")
    
    def add_annual_interest(self):
        prev_bal = self.__balance
        new_bal = prev_bal * BankAccount.INTREST_RATE / 100
        self.__balance += new_bal
        return f"Interest added: {new_bal}"
    
    @staticmethod
    def is_valid_amount(amount):
        return True if amount > 0 else False

    

    def __str__(self):
        return f"Account[{self.name}] {self.name} | {self.account_type} | Rs.{self.__balance:,.2f}"




            



        
