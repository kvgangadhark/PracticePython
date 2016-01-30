#Take two lists, say for example these two:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that are common between the lists (without duplicates).
output_list = []

for each in a:
    if (each in b) and (each not in output_list):
        output_list.append(each)

print (output_list)


