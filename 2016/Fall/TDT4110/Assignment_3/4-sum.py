#Oppgave a)

N,x = int(input('Give me the number N, where to stop: ')),0
for i in range(1,N+1):
    x+=1/i**2
print ('After',N,'iterations, the variable x is:',format(x,'.2f'))

#Oppgave b)
x,i,tol=0,1,float(input('What should be the tolerance?: '))
while True:
    y=x
    x+=1/i**2
    x_change=x-y
    i+=1
    if x_change<tol:
        print ('With the tolerance of',tol,'the x =',format(x,'.2f'))
        break
