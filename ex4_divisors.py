# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. 
# number that divides evenly into another number.

divisors=[]
user_input = int(input("enter a number to get the list of its divisors:"))
index = 1

while index < user_input:
	if user_input % index == 0:
		divisors.append(index)
	index+=1

print (divisors)
