c = []
def count_c(c):
    return sum(c[i] for i in range(len(c)))

#print(count_c([5,10,20,1,1,10]))

def n_c(n):
    p = [[] for i in range(len(n))]
    for i in range(len(n)):
        p[i].append(n[i]//20)
        n[i]=n[i]%20
        p[i].append(n[i]//10)
        n[i]=n[i]%10
        p[i].append(n[i] // 5)
        n[i] = n[i] % 5
        p[i].append(n[i])
    return p
print(n_c([12,23]))
