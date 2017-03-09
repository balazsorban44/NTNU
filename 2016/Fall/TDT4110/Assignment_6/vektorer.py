from math import sqrt
def vector(a,b,c):
    return [a,b,c]
print(vector(1,2,3))

def vectornice(a,b,c):
    print ('vec1 =',vector(a,b,c))
vectornice(1,2,3)

def scalar(list,s):
    vec2=[None]*len(list)
    for i in range(len(list)):
        vec2[i]=list[i]*s
    return vec2
print(scalar([1,2,3],4))

def length(list):
     return sqrt(sum(list[x]**2 for x in range(len(list))))
print(length([1,2,3]))

def innerproduct(list1,list2):
    list3=[None]*len(list1)
    for i in range(len(list1)):
        list3[i]=list1[i]*list2[i]
    return list3
print(innerproduct([1,2,3],[1,2,3]))
