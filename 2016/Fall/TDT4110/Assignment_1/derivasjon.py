import string
import math
h = float(input('What is h?: '))
x = float(input('What is x?: '))
f1 = math.sin(x)
f2 = math.sin(x+h)
derivative = (f2 - f1)/h
print(format(derivative,'.2f'))
