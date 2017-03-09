#Oppgave a)
sum,z,k=1,0,int(input('Give me the k^th element of the Fibonacci series:'))
for x in range(0,k):
    y=sum+z
    sum=y-sum
    z=y
print('The k^th number of Fibonacci series is:',sum)

#Oppgave b)
sum,z,k_sum,k=1,0,0,int(input('Give me the k^th element of the Fibonacci series:'))
for x in range(0,k):
    y=sum+z
    sum=y-sum
    z=y
    k_sum+=sum
print('The sum of the first k number of Fibonacci series is:',k_sum)

#Oppgave c)

sum,z,k=1,0,int(input('Give me the k^th element of the Fibonacci series:'))
k_sum= []
for x in range(0,k):
    y=sum+z
    sum=y-sum
    z=y
    k_sum.append(sum)
    print(k_sum[x])
