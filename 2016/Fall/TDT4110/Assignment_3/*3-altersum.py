#Oppave a)
i,n = 0,int(input('Give me a whole number:'))
for x in range(1,n+1):
    if x%2==0:
        i-=x**2
    else:
        i+=x**2
print ('The sum of the first',n,'number in the series:',i)

#Oppave b)
tempsum=0
sumlist,x,sum,k = [],0,0,int(input('Stop me when the sum of the series is smaller than this number:'))
while True:
    if x%2==0:
        tempsum-=x**2
    else:
        tempsum+=x**2
    #sumlist.append(sum)
    if tempsum>k:
        print ('The least sum of the series under',k,'is',sumlist[x-1],'The series has',x-1,'elements.')
        break
    else:
        sum=tempsum
    x+=1
