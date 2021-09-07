def build_profile(first, last, **user_info):
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print(user_profile)

"""

В ООП конструктором класса называют метод, который автоматически вызывается при создании объектов.
Python же роль конструктора играет метод __init__()

В Python наличие пар знаков подчеркивания спереди и сзади в имени метода говорит о том, что он принадлежит к 
группе методов перегрузки операторов. Если подобные методы определены в классе, то объекты могут участвовать в 
таких операциях как сложение, вычитание, вызываться как функции и др.

"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")


my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()
your_dog = Dog('Lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        self.odometer_reading = mileage
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")


my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(23)
my_new_car.read_odometer()

my_used_car = Car('subaru', 'outback', 2015)

print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()