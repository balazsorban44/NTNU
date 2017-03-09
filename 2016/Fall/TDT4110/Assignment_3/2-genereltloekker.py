#Oppgave a)
j,sum=0,0
while j<100:
    j+=1
    sum+=j
else:
    print ('Summen av de 100 foerste tallene er',sum)

#Oppgave b)
i,product=1,1
while product<1000:
    product*=i
    i+=1
else:
    print ('Loekken kjoerte',i,'ganger, produktet ble',product)

#Oppgave c)
while i != 12:
    i=int(input('    What is 3*4?: '))
else:
    print ('You are right, 3*4 is 12.')
