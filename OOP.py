from abc import ABC, abstractmethod

class Car:
    def __init__(self, brand, colour,):
        self.brand = brand   # Attribute
        self.colour = colour # Attribute

    def drive(self):
        print(f"The { self.colour} { self.brand} is driving.")

# Creating an object (instance of car)
my_Car = Car("Toyota", "Red")
my_Car2 = Car("BENZ", "Blue")
print(my_Car.brand)
my_Car.drive()

# ENCAPSULATION
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def set_balance(self, amount):
        if balance < 0:
            raise ValueError("Balance cannot be negative.")
        self.__balance = amount


# Creating an object
account = BankAccount(1000) # setting a new balance
print(account.get_balance())# output: 1000

account.set_balance(2000)    # setting a new balance
print(account.get_balance()) # output: 2000

# account.set_balance(-500)  # Raise a valueError
# print(account.__balance)   # Error: Cannot access private attribute

# INHERITANCE
# Single Inheritance
# Parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "I make a sound."

# child class (inherits from animal)- Dog inherits from animal, meaning dog can use animal attribute and methods.
# The Dog class overrides the speak() method to provide its can implementation
class Dog(Animal):
    def speak(self):
        return "Woof! Woof!"

# creating an object of dog
dog = Dog("Buddy")
print(dog.name)
print(dog.speak())

# Parent CLass
class Appliance:
    def __init__(self, brand):
        self.brand = brand

    def function(self):
        return "The appliance has a function."

# Child class
class WashingMachine(Appliance):
    def __init__(self, brand, capacity):
        super().__init__(brand)
        self.capacity = capacity

    def function(self):
        return "The washing machine washes clothes."

# Creating an object of washing machine
machine = washingmachine("Whirlpool", "7kg")
print(machine.brand)
print(machine.capacity)
print(machine.function())

# Multiple Inheritance (one child, Multiple
# Parent Class 1
class Animal2:
    def __init__(self, name):
        self.name = name

    def  eat(self):
        return f"{self.name} is eating"

# Parent class 2
class Pet:
    def play(self):
        return "Playing with  owner."

# Child class (inherits from Animal and Pet)
class Dog2(Animal, Pet):
    def speak(self):
        return "Woof! Woof!"

# Creating an object of Dog
dog2 = Dog2("Buddy")
print(dog2.eat())
print(dog2.play())
print(dog2.speak())

# Multilevel inheritance (A child inherits from Another child)
class LivingBeing:
    def breathe(self):
        return "Breathing oxygen"

class Mammal(LivingBeing):
    def warm_blooded(self):
        return " I am Warm blooded"

class Dolphin(Mammal):
    def swim(self):
        return "I Can Swim."

# Object for Dolphin
flipper = Dolphin()
print(flipper.swim())
print(flipper.warm_blooded())
print(flipper.breathe())