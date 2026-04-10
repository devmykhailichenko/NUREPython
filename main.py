# Модулі, ООП початок
import helpers as hp
import sys

x = 10

def hello():
    print("Hello")

# print(__name__)
# print(__file__)
# print(globals())

hp.greetings_from_module()
sys.path.insert(0, '/Users/ihormykhailichenko/Desktop/')
print(sys.path)

print(hp.NUMBER, hp.add(4, 5))

# public private protected
class Car:
    def __init__(self, brand, model, color, max_speed, secret_number):
        self.brand = brand
        self.color = color
        self.max_speed = max_speed
        self.model = model
        self.speed = 0
        self.__secret_engine_number = secret_number #private
        self._car_number = 1

    def drive(self):
        self.speed = 100
        print(f"Car {self.model} is on a way!", self.__secret_engine_number, self._car_number)

    def stop(self):
        self.speed = 0
        print(f"Car {self.model} stopped!")


car_1 = Car("BMW", "x7", "red", 300, 3434)
car_2 = Car("Toyota", "CHR", "white", 200,3434)

car_1.drive()
car_2.drive()
car_1.stop()