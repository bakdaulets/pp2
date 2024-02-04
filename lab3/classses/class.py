#1
class getString():
    def __init__(self):
        self.str1 = ""
    def getString(self):
        self.str1 = input()
    def printString(self):
        print(self.str1.upper())

str1 = getString()
str1.getString()
str1.printString()

#2
class Shape:
    def area(self):
        return 0
class square():
    def __init__(self,length):
        self.length1 = length

    def area(self):
        return self.length1 ** 2
    
#3
class rectangle(shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(seld):
        return self.length * self.width
    
#4
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        return self.x , self.y
    def move(self, x, y):
        self.x += x
        self.y += y
    def dist(self):
        return ((self.x - delf.x)**2 + (self.y- delf.y)**2)**0.5
    
#5
class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def Deposit(self, amount):
        self.balance += amount
    def Withdraw(self, amount):
        if amount<= self.balance:
            self.balance -= amount
        else:
            print("No")

#6
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

numbers = []
n = int(input())
for i in range(n):
    num = int(input())
    numbers.append(num)
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)