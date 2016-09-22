a = int(input('\n    Give me a number: '))
b = int(input('    Give me another one: '))
c = int(input('    And a third one: '))
d = b**2 - 4*a*c

print('\n    Your equation is: ',a,'(x^2)+',b,'x+',c, sep='')

if d < 0:
    print('\n    There are two imaginary roots for this equation.')
elif d == 0:
    print('\n    There is one real root for this equation.')
else:
    print('\n    There are two real roots for this equation.')
