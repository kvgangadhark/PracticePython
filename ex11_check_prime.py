#write a function to chek primality of a given number

def get_number():
    return int(input("enter the number to check for primality:"))

def is_prime(number):
    index = int(number / 2)
    while index >=2:
        print ("index is "+str(index) +"num is "+ str(number))
        if (number % index) == 0:
            return 0
        index -= 1
    return 1

num = get_number()
if (is_prime(num) == 0):
    print("number is not prime")
else:
    print("number is prime")
