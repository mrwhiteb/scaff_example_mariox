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
