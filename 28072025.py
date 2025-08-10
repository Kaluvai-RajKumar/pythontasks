from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def deposit(self):
        pass
    @abstractmethod
    def withdraw(self):
        pass
class union(Bank):
    def __init__ (self):
        self.balance=0
    def deposit(self,amount):
        self.balance += amount
        print(self.balance)
    def withdraw(self,amount):
        if amount < self.balance:
            self.balance -= amount
            print(self.balance)
        else:
            print("Check Your Balnace")
obj=union()
obj.deposit(300000)
obj.withdraw(198345)
obj.withdraw(4000000)