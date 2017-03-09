def recursive_sum(n):
    if (n==0):
        return 0
    else:
        return n + recursive_sum(n-1)

print(recursive_sum(5))





def find_smallest_element(n):
    if (len(n) == 1):
        return n[0]
    else:
        m = find_smallest_element(n[1:])
        if m < n[0]:
            return m
        else:
            return n[0]


print(find_smallest_element([5,4,3,2,5]))
