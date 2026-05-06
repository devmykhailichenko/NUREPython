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

    def __add__(self, right_car):
        total_speed = self.speed + right_car.speed
        return f"{self.brand} + {right_car.brand} = {total_speed}"

    def __len__(self):
        return self.max_speed

    def __str__(self):
        return f"{self.brand} is {self.color} color and can move with {self.max_speed} km/h"

    def drive(self):
        self.speed = 100
        print(f"Car {self._car_number} / {self.model} is on a way!")

    def stop(self):
        self.speed = 0
        print(f"Car {self.model} stopped!")

    @property
    def secret_engine_number(self):
        return self.__secret_engine_number

    @secret_engine_number.setter
    def secret_engine_number(self, new_engine_number):
        if new_engine_number < 0:
            print("Invalid number!")
        else:
            self.__secret_engine_number = new_engine_number

    def get_engine_number(self):
        return self.__secret_engine_number

    def set_engine_number(self, new_engine_number):
        if new_engine_number < 0:
            print("Invalid number!")
        else:
            self.__secret_engine_number = new_engine_number


car_1 = Car("BMW", "x7", "red", 300, 3434)
car_2 = Car("Toyota", "CHR", "white", 200,3434)

car_1.drive()
car_2.drive()
car_1.stop()


car_1.secret_engine_number = 10
print(car_1.secret_engine_number)

car_1.secret_engine_number = -7
print(car_1.secret_engine_number)

class ElectricCar(Car):
    def __init__(self, brand, model, color, max_speed, secret_number, battery_capacity):
        super().__init__(brand, model, color, max_speed, secret_number)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"{self.brand} is charging")

    def drive(self):
        self.speed = 110
        print(f"{self.brand} is driving without any noise!")


class Truck(Car):
    def __init__(self, brand, model, color, max_speed, secret_number, load_capacity):
        super().__init__(brand, model, color, max_speed, secret_number)
        self.load_capacity = load_capacity

    def load_cargo(self):
        print(f"Truck is loading for max {self.load_capacity} kg")

    def drive(self):
        super().drive()
        self.speed = 70
        print(f"{self.brand} is moving with {self.load_capacity} capacity!")


electric = ElectricCar("Tesla", "Y", "white", 300, 40, 10000)
truck = Truck("Mercedes", "TR-1", "grey", 90, 12, 2000)

#{}.__init__() -> {brand:"", color:"", drive, stop}["battery_capacity"] = 34 -> {brand:"", color:"", drive, stop, "battery_capacity", charge}

# cars = [car_1, car_2, electric, truck]
#
# for car in cars:
#     car.drive()

#dunder methods __str__ __len__ __add__ __eq__

print(car_1 + car_2)
print(car_1)
print(len(car_2))