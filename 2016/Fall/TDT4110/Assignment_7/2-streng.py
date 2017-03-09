def check_equal(str1, str2):
    '''
    for i in range(len(str1)):
        return False if len(str1) != len(str2) else True if str1[i] == str2[i] else False
    '''

    #return False if len(str1) != len(str2) else all(True if str1[i] == str2[i] else False for i in range(len(str1)))

    return str1 == str2

#print(check_equal('hei','hei'),check_equal('he','hei'),check_equal('ei','hei'))

def reversed_word(str1):
    str1=list(str1)
    for i in range(1,len(str1),2+len(str1)%2): # ???? :D
        str1[-i],str1[i-1]=str1[i-1],str1[-i]
    return ''.join(str1)

'''
def reversed_word(str1):
    str2=""
    for i in range(len(str1)-1, -1, -1):
        str2 += str1[i]
    return str2
'''

#print(reversed_word('pneumonoultramicroscopicsilicovolcaniosis'))

def check_palindrome(str1):
    return str1 == reversed_word(str1)

#print(check_palindrome('retipipiter'))

def contains_string(str1, str2):
    return str1.index(str2) if str2 in str1 else -1
print(contains_string('pepperkake','per'),contains_string('pepperkake','ola'))
