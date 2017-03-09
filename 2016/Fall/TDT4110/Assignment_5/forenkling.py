def gcd(a,b):
    while b!=0:
        old_b=b
        b=a%b
        a=old_b
        #a,b=b,a%b
    return a
print(gcd(30,20))

def reduce_fraction(a,b):
    return int(a/gcd(a,b)),int(b/gcd(a,b))

print(reduce_fraction(42,13)[0],'/',reduce_fraction(42,13)[1])
