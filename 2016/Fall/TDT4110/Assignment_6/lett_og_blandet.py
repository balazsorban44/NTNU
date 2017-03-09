import math
def isSixtAtEdge(list):
    return list[0]==6 or list[-1]==6

print(isSixtAtEdge([6,0,0,0,6]))

def average(list):
    return sum(list)/len(list)

print(average([1,2]))

def median(list):
    list.sort()
    return list[int((len(list)/2))]

print(median([1,3,6,5,2,4,9,8,7,10,11]))
