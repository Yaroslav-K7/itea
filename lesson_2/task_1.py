class Car:
    fuel_tank = 1
    material = "iron"

    def drive(self):
        print("go straight")

    def get_fuel(self):
        print(f"get fuel into {self.fuel_tank}")

class PassengerCar(Car):
    capacity_fuel_tank = 40
    fuel_consumption = 10

    def drive(self):
        print(f"Go straight. Fuel reserves will last: {round(self.capacity_fuel_tank / self.fuel_consumption, 2)} hours")


    def get_fuel(self):
        print(f"get gasoline into {self.fuel_tank}")


class Truck(Car):
    fuel_tanks = 2
    capacity_fuel_tank= 120
    fuel_consumption = 14
    def drive(self):
        print(f"Go straight. Fuel reserves will last: {round(self.capacity_fuel_tank / self.fuel_consumption, 2)} hours")


def get_fuel(self):
        print(f"get diesel into {self.fuel_tanks}")
