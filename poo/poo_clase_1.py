"""import sys

class CarRojo:
    key = '123'

def main():
    car = CarRojo()
    car2 = CarRojo()
    car.key = '321'
    print(car.key,car2.key)

if __name__ == '__main__':
    sys.exit(main())"""

"""import sys


class CarRojo:
    def __init__(self, key):
        self.key = key


def main():
    car = CarRojo('123')
    car2 = CarRojo('321')
    print(car.key, car2.key)


if __name__ == '__main__':
    sys.exit(main())
    """
"""import sys

class CarRojo:
    def __init__(self,key='000',max_kmh=180):
        self.key = key
        self.max_kmh = max_kmh

def main():
    car1 = CarRojo('123')
    print(car1.key,car1,car1.max_kmh)

if __name__ == '__main__':
    sys.exit(main()) """

"""herencia simple
import sys


class Vehicle:
    def acelerar(self):
        print('acelerar')
class Acuatic(Vehicle):
    def __init__(self,nombre):
        self.name=nombre


def main():
    felix = Acuatic ('Sea-Doo Perros')
    print(felix.name, felix.acelerar())


if __name__ == '__main__':
    sys.exit(main())"""

import sys


class Vehicle:
    def acelerar(self):
        print('acelerar')
    def frenar(self):
        print('frena')

class Acuatic(Vehicle):
    def __init__(self,marca):
        self.__brand=marca
    def dive(self):
        print('glup glup')

class LandVehicle(Vehicle):
    def llantas(self):
        print('llantas')

class MotoAcuatic(Acuatic):
    def __init__(self, modelo):
        self.model = modelo

def get_name(self):
    return self.__brand

def diving(x):
    print(x.dive())

def main():
    jetski = Acuatic('Nissan ')
    print(jetski._Acuatic__brand)  #encapsulamiento
    jetski: Vehicle = MotoAcuatic(jetski)
    print(diving(jetski)) #polimorfismo
    jetski = MotoAcuatic('Sea-Doo ') #Herencia
    print(jetski.model)
if __name__ == '__main__':
    sys.exit(main())
