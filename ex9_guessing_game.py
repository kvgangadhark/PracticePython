import random

num = random.randint(1,10)

print (num)

choice = " "
def loop1():
	while 1:
		choice = input("guess the number:")
		if choice == "exit":
			print("bye loser!")
			return
		inp=int(choice)
		if inp < num:
			print(" u r guessing low")
		elif inp > num:
			print("u guess too high")
		else:
			print("u won!")
			return

loop1()
