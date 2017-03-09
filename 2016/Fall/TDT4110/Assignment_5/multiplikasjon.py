def functionA(tol):
    count=1
    prod=1+(1/(count**2))
    run=True
    while run:
        count+=1
        change=prod
        prod*=(1+(1/(count**2)))
        change=prod-change
        if tol>change:
            run=False
    return (prod,count)
print('The product is',format(functionA(0.01)[0],".2f"),'after',functionA(0.01)[1], 'iterations.')


def functionB(tol):
    count=1
    prod=1+(1/(count**2))
    run=True
    while run:
        count+=1
        change=prod
        prod*=(1+(1/(count**2)))
        change=prod-change
        if tol>change:
            run=False
    return (prod,count)
print('The product is',format(functionB(0.01)[0],".2f"),'after',functionB(0.01)[1], 'iterations.')
