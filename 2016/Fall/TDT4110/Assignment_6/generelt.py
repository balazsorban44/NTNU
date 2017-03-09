my_first_list = list(range(1,7))
print(my_first_list[-1])

my_first_list[-2]='plus'

my_second_list = my_first_list[-3:]

for x in range(len(my_second_list)):
    print(my_second_list[x],end=' ')
print('equals 10.')
