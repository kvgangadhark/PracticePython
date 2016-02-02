#Generate a random 4 digit number and ask the user to guess it.
#if the guesssed number is having x digits correct in the correct location we will  return x cows and if the guess has y digits correct in the wrong position we will retun y bulls. 
# Continue the game till he guesse o enters 0

import random

_random_number = random.randint(1000,9999)
#print (random_number) 

index = 4 # since this is a 4 digit number we are using 4 here, if you want a n digit number change inde to b.

_divisor = 10
def cows_n_bulls(random_number):
	cows = 0
	bulls = 0
	guess = int(input("guess the numer:"))
	if guess < 1000:
		return 1

	print(random_number)
	counter = index
	divisor = 10
	digits_random = []
	digits_guess = []
	while counter > 0:
		if (random_number % divisor == guess % divisor):
			cows += 1
		digits_random.append(random_number % divisor)
		digits_guess.append(guess % divisor)
		random_number /= 10
		guess /= 10
		counter -= 1
	for each in digits_random:
		if each in digits_guess:
			bulls+=1
	bulls -= cows
	print (cows)
	print(bulls)
	if (cows == index):
		return 1
	else:
		return 0

ret = 0
while ret != 1:
	ret = cows_n_bulls(_random_number)



