#ask the user to input a number and print if it is even or odd.

number = int(input("enter a numner:"))
if number %2 == 0:
    if number %4 == 0:
        print ("divided by 4")
    else:
        print ("even")
else:
    print ("odd")
