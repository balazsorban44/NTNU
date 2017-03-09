
name = input("Hei jeg er THE DOORMAN. What is your name? ")
age = int(input("What is your age? "))
drunk = input("Are you drunk? Yes, or No? ")

if age>=18:
    if drunk=="Yes":
        print("You are drunk, sorry.")
    else:
        print("You are in",name)
else:
    print("You are too young")
