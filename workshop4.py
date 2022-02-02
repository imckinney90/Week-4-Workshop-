from ast import Str
from os import name


class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, name):
        self.name = name

    def change_pin(self, pin):
        self.pin = pin

    def change_password(self, password):
        self.password = password


class BankUser(User):
    def __init__(self, name, pin, password):
        super().__init__(name, pin, password)
        self.balance = 0

    def show_balance(self, balance):
        self.balance = balance
        print(user.name, "has an account balance of:", user.balance)

    def withdraw(self, balance):
        self.balance -= balance

    def deposit(self, balance):
        self.balance += balance


  # Driver Code for Task 1
"""
    class User():
        def __init__(self, name, pin, password):
            self.name = name
            self.pin = pin
            self.password = password


user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password) """

# Driver Code for Task 2

""" user = User("Bob", 1234, "password")
print(user.name, user.pin, user.password)
user.change_name("Bobby")
user.change_pin("4321")
user.change_password("newpassword")
print(user.name, user.pin, user.password) """

# Driver Code for Task 3
""" user = BankUser("Bob", 1234, "password")
print(user.name, user.pin, user.password, user.balance)
 """

# Driver Code for Task 4
user = BankUser("Bob", 1234, "password")
print(user.name, user.pin, user.password, user.balance)


""" # user.show_balance(user.balance)
print(user.name, "has an account balance of:", user.balance)
# print(user.name, "has an account balance of:", user.balance + 1000) """
