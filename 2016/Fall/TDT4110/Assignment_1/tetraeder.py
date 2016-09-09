import math
h = int(input('What is the sidelength: '))
a = (3/math.sqrt(6))*h
print ('You choose the sidelength to be', h,'therefore the volume is',round(math.sqrt(3)*math.pow(a,2),2),'and the area is',round(math.sqrt(2)*math.pow(a,3)/12,2))
