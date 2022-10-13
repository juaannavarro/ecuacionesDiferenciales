from clases.ecuaciones import *
import sympy
import math 
x = sympy.Symbol('x')
y = sympy.Function('y')


class Ecuaciones:
    def __init__(self, ec1, ec2, ec3, ec4):
        self.ec1 = ec1
        self.ec2 = ec2
        self.ec3 = ec3
        self.ec4 = ec4
        pass
    def resolver_Ec(self):
        while True:
            print("Ecuaciones diferenciales de primer orden")
            print("1. y' = x^2y - y / y + 1")
            print("2. y' = yln(y) / sen(x)")
            print("3. y' = 2(x-2)^2 + y / (x-2)")
            print("4. y' = (y+3x^2) / 2x")
            print("5. Salir")
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                self.ec1()
            elif opcion == 2:
                self.ec2()
            elif opcion == 3:
                self.ec3()
            elif opcion == 4:
                self.ec4()
            elif opcion == 5:
                break
            else:
                print("Opción inválida")
Ecuaciones(ec1,ec2,ec3,ec4).resolver_Ec()