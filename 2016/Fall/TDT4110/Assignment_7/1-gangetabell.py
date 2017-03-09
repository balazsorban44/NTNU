def separate(n, t):
    l1,l2=[],[]
    for i in range(len(n)):
        l1.append(n[i]) if n[i] < t else l2.append(n[i])
    print('separate([1,2,3,4,5,6,7,8,9],5)\n',l1,l2,'\n',sep='')
    #return ([n[i]] if n[i]< t else [n[i]] for i in range(n))
separate([1,2,3,4,5,6,7,8,9],5)


def multiplication_table(n):
    return [[x*y for x in range(1,n+1)] for y in range(1,n+1)]

print('\nmultiplication_table(4)\n',multiplication_table(4),'\n',sep='')
