# Reverse of the guessing game we have written earier.

start = 1
end = 100
found = False
while found != True:
    guess = int((start + end ) / 2)
    print (guess)
    inp = int(input("enter 1: too low, 2: too high, 3: correct!"))
    if inp == 3:
        print ("bye!")
        found = True
    elif inp == 1:
        start = guess
        guess = min1(end, guess + comp)
    else:
        end = guess
        guess = max1(start, guess - comp)
