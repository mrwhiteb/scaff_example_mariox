import builtins
import sys
import transformations.transform as t
from transformations.transform import number, Animal
#El main es el punto de entrada
def main():
    b = t.Animal()
    b.correr()
    print(number)

    print(t.suma(9,9))
    return 0

if __name__ == '__main__':
    sys.exit(main())
