import random

numbers=[i for i in range(1,35)]


myGuess=[int(input()) for i in range(7)]
randoms = []

def pick():
    for i in range(10):
        randoms.append(random.randint(1,len(numbers)))
    return randoms

def compList(list1,list2):
    z=0
    for i in range(len(list1)):
        for j in range(len(list2)):
            if list1[i]==list2[j]:
                z+=1
    return z
def prize(same,extra):
    if same == 7:
        print('You won 2 749 455 kr!!!!')
    elif same == 6 and extra==1:
        print('You won 102 110 kr!')
    elif same == 6:
        print('You won 3 385 kr!')
    elif same == 5:
        print('You won 95 kr!')
    elif same == 4 and extra==1:
        print('You won 45 kr!')
    else:
        print('You are bad at lotto. Try something else, before you hurt yorself!')

prize(compList(myGuess,pick()[:7]),compList(myGuess,pick()[7:]))
