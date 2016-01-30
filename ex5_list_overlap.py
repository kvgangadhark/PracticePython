#Take two lists and print the common elements in the two lists.
list_a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list_b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
final_list = []

for each in list_a:
	if each in list_b:
		final_list.append(each)

print (final_list)
