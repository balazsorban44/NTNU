def function(age):
    if age < 5 or age > 60:
        return 0
    elif 5 <= age <= 20:
        return 20
    elif 21 <= age <= 25:
        return 50
    elif 26 <= age <= 60:
        return 80
print(function(4))
print(function(5))
print(function(20))
print(function(21))
print(function(25))
print(function(60))
print(function(61))
