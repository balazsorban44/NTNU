import random
random_numbers = [random.randint(0,9) for i in range(100)]
print("Number of 2's:",random_numbers.count(2),'Sum of numbers:',sum(random_numbers),sep='\n')

print('Sorted:',sorted(random_numbers),'Most common element:',max(set(random_numbers), key=random_numbers.count),sep='\n')


print('Reversed:',list(reversed(sorted(random_numbers))),sep='\n')
