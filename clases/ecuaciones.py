import sympy
import math 
x = sympy.Symbol('x')
y = sympy.Function('y')



def ec1():
        print("ECUACIÓN 1")
        global x, y
        f = x**2*y(x)-y(x) / y(x)+1
        sympy.Eq(y(x).diff(x), f)
        sympy.dsolve(y(x).diff(x) - f)
        sympy.dsolve(y(x).diff(x) - f, ics={y(3): -1})
        print(sympy.dsolve(y(x).diff(x) - f))
        print(sympy.dsolve(y(x).diff(x) - f, ics={y(3): -1}))
ec1()
def ec2():
        global x , y 
        print("ECUACIÓN 2")
        f1= y(x)*sympy.log(y(x))/sympy.sin(x)
        sympy.dsolve(y(x).diff(x) - f1)
        sympy.dsolve(y(x).diff(x) - f1, ics={y(math.pi/2): math.e})
        print(sympy.dsolve(y(x).diff(x) - f1))
        print(sympy.dsolve(y(x).diff(x) - f1, ics={y(math.pi/2): math.e}))
ec2()
def ec3():
        global x, y
        print("ECUACIÓN 3")
        f2 = 2*(x-2)**2 + y(x)/(x-2)
        sympy.dsolve(y(x).diff(x) - f2)
        print(sympy.dsolve(y(x).diff(x) - f2))
ec3()
def ec4():
        print("ECUACIÓN 4")
        f3 = (3*x**2)+y(x)/(x*2)
        sympy.dsolve(y(x).diff(x) - f3)
        print(sympy.dsolve(y(x).diff(x) - f3))
        f4 = (y(x)+3*x**2)/2*x
        p = sympy.dsolve(y(x).diff(x) - f4)
        print("Familia de soluciones generales de la ecuación diferencial y'= (y+3x^2) / 2x", p )
ec4()
