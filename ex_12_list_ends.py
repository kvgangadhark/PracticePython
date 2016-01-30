#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.

list_a = [1,2,3,4,5,6,7,12,23,45,67,89,76]

length = len(list_a)
print (length)
new_list=list_a[::length-1]
print (new_list)
