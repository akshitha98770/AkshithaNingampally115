'''
Abstraction: it hides the internal implementation, shows the essential functions to the user
ex: phone pay,vehicel,ATM  
'''
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def sound(self):
        print("Vehicle gives sound")
class Car(Vehicle):
    def sound(self):
        print("Car make sound")
v = Vehicle()
v.sound()
c = Car()
c.sound()
