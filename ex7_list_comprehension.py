#starting list comprehension. creating a list from a list basing on a condition.

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# since there is no calirty in the question we have to for two solutions.
#first one collects the even numbers in the list to the new list.
#second one collects the alternate numbers such that the numbers in even position are added to the new list.

b = [each for each in a if each %2 == 0]
print(b)
b = a[::2]
print (b)
