from abc import ABC, abstractclassmethod


class Vehicle(ABC):
    pass

    @abstractclassmethod
    def start(self):
        pass

    @abstractclassmethod
    def move(self):
        pass


class Car(Vehicle):

    def start(self):
        print('Car Started')

    def move(self):
        print('Car Moved')


class Motocycle(Vehicle):

    def start(self):
        print('Motocycle Started')

    def move(self):
        print('Motocycle Moved')


class Horse(Vehicle):

    def move(self):
        print('Motocycle Moved')


def vehicle_move(vehicle):
    vehicle.start()
    vehicle.move()

car = Car()
vehicle_move(car)

m = Motocycle()
vehicle_move(m)

horse = Horse()

vehicle_move(horse)