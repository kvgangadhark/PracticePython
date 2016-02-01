# Reverse of the guessing game we have written earier.

guess = 50
found = False
comp = guess
while found != True:
    if guess == 0 or guess == 100:
        print("error closing")
        found = True
    print (guess)
    comp =int(guess/2)
    inp = int(input("enter 1: too low, 2: too high, 3: correct!"))
    if inp == 3:
        print ("bye!")
        found = True
    elif inp == 1:
        guess += comp
    else:
        guess -= comp


