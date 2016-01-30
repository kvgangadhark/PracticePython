
#this function returns 1 if a wins, 0 if b wins
def rock_paper_scissors(a,b):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"
    if (a == rock and b == scissors) or (a == paper and b == rock) or (a == scissors and b == paper):
        return 1
    else:
        return 0

choice = 'y'
while choice != 'n':
    a = input("enter choice of a:")
    b = input("enter choice of b:")
    ret = rock_paper_scissors(a,b)
    if ret == 1:
        print(" a wins")
    else:
        print ("b wins")
    choice = input("do you want to try again(y/n):")

print ("bye!")
