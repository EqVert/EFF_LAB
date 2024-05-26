class Customer:
    def __init__(self, account):
        self.account = account

    def get_account(self):
        return self.account

class Account:
    def __init__(self, balance):
        self.balance = balance

    def get_balance(self):
        return self.balance

class Bank:
    def __init__(self, customer):
        self.customer = customer

    def get_customer(self):
        return self.customer
        
    # Метод get_customer_balance інкапсулює ланцюжок викликів, 
    # зменшуючи зв'язність між класами та спрощуючи доступ до балансу
    def get_customer_balance(self):
        return self.customer.get_account().get_balance()

# Використання методу, що інкапсулює ланцюжок викликів
bank = Bank(Customer(Account(1000)))
balance = bank.get_customer_balance()
print(f"The balance is: {balance}")
