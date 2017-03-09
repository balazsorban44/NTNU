#Oppgave a)
for x in range(1,5):
    print('\n',x,'time:',end=' ')
    for y in range(1,5):
        print(x*y,end=' ')
#Oppgave b)
print('\n')
for x in range(2,100):
    for y in range(2,x):
        if (x%y)==0:
            break
    else:
        print (x,end=' ')
