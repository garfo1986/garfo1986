from mimetypes import init


class Vehicle():
    def __init__(self, color) -> None:
        self.color = color
        self.wheels = 4
        self.doors= 5

class car(Vehicle):
    speed = 120
    cylinder = True

mazda =(car("white"))

print(f"my car is a {mazda.color} car, its top speed is {mazda.speed}, it has {mazda.doors} doors and {mazda.wheels} wheels ")