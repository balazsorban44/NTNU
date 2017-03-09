# Oppgave a
a = int(input('\n    Give me a number: '))
b = int(input('    Give me another one: '))

if a+b < a*b :
    print('\n    a+b is smaller than a*b')
elif a+b == a*b :
    print('\n    a+b equals to a*b')
else:
    print('\n    a*b is smaller than a+b')

# Oppgave b
c = int(input('\n    Tell me what is 3 times 4?: '))
if c == 12:
    print('\n    You are a smart one, you!')
else:
    print('\n    You should practice math... :/ ')
