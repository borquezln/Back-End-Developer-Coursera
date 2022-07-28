# Import ABC and abstractmethod from the module abc
from abc import ABC, abstractmethod

# Abstract class Bank
class Bank(ABC):
    def basicinfo(self):
        print("This is a generic bank")
        return "Generic bank: 0"
    
    @abstractmethod
    def withdraw(self):
        pass

# Class Swiss that derives from class Bank
class Swiss(Bank):
    def __init__(self) -> None:
        super().__init__()
        self.bal = 1000
    
    def basicinfo(self):
        print("This is the Swiss Bank")
        return "Swiss Bank: " + str(self.bal)
    
    def withdraw(self, amount):
        if self.bal >= amount:
            self.bal -= amount
            print(f"Withdrawn amount: {amount}")
            print(f"New Balance: {self.bal}")
            return self.bal
        else:
            print("Insufficient funds")
            return self.bal

# Function main
def main():
    assert issubclass(Bank, ABC), "Bank must derive from class ABC"
    s = Swiss()
    print(s.basicinfo())
    s.withdraw(30)
    s.withdraw(1000)

if __name__ == "__main__":
    main()