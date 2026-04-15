class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("Driving on the road")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling on the road")

# Example
v1 = Car()
v2 = Bicycle()

v1.move()
v2.move()
import math

def circle(radius):
    return math.pi * radius * radius

def rectangle(l, w):
    return l * w

def triangle(b, h):
    return 0.5 * b * h
