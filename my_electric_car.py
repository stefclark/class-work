from car import ElectricCar

my_car = ElectricCar('anything but a tesla', 'model not a tesla', '2018')

print(my_car.get_descriptive_name())
my_car.battery.describe_battery()
my_car.battery.get_range()