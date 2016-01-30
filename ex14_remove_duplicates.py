#take a list as input and create a new list with unique elements from it.

a = [1,2,3,4,5,1,2,3,4,5,1,12,23,4,4,56,67,12]

b = []

for each in a:
    if each not in b:
        b.append(each)

print (b)
