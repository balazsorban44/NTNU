def add_data(user):
    user = user.split(' ')
    user[2]=int(user[2])
    return user

#print(add_data('Balazs Orban 21 Male Partner'))



def get_person(given_name, list1):
    '''facebook = [
                ["Mark", "Zuckerberg", 32, "Male", "Married"],
                ["Therese", "Johaug", 28, "Female", "Complicated"],
                ["Mark", "Wahlberg", 45, "Male", "Married"],
                ["Siv", "Jensen", 47, "Female", "Single"],
                ]
    result = []
    for i in range(len(facebook)):
        if given_name in facebook[i]:
            result.append(facebook[i])
    return result
    #return [list(filter(lambda x: given_name in list1[i]    ,list1[i])) for i in range(len(list1))]   <-- MIN
    '''
    return list(filter(lambda x: x[0]==given_name,list1))
    #return [x for x in list1 if x[0]==given_name]
#print(get_person('Mark',facebook))


def main():
    facebook,stop=[],False
    while not stop:
        data=input('Add a new user by writing "given_name surname age gender relationship_status": \n')
        if data != 'done':
            facebook.append(add_data(data))
        else:
            while True:
                result=input('Search for user: ')
                if result != 'done':
                    print(get_person(result,facebook))
                else:
                    print('Bye!')
                    stop=True
                    break
main()
