import math
def f(x):
    return (x-12)*math.exp(5*x)-8*(x+2)**2
print(f(0))


def g(x):
    return -x-2*x**2-5*x**3+6*x**4
print(g(1))

def derivate(h,x,func):
    return float((func(x+h/2)-func(x-h/2))/h)
print(derivate(0.000001,-2,f))

def newtons_method(h,x,func,tol):
    while 
