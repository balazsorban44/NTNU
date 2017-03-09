#Oppgave a)
sum,i=0,0
r=float(input('Give me a number between -1 and 1: '))
n=int(input('How many times should I run?: '))
while True:
    sum+=r**i
    if i==n:
        print('The sum of the series is',sum,'.')
        break
    i+=1

#Oppgave b)

sum,i=0,0
r=float(input('Give me a number between -1 and 1:'))
tol=float(input('What is the tolerance?:'))
while True:
    sum+=r**i
    i+=1
    if (1/(1-r))-tol<sum:
        print('To be in the tolerance of ',tol,', this loop ran ',i,' times.\n','The difference between the real and estimated value was ',(1/(1-r))-sum,'.',sep='')
        break
