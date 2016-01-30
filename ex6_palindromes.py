# Take a string from user and check if it is a palindrome or not.

string_to_check = input("enter the string to check:")
new_string=[]

index = len(string_to_check) -1

while index >= 0:
    new_string.append(string_to_check[index])
    index -= 1
print("reversed string is " + ''.join(new_string))

if (''.join(new_string)) == string_to_check:
    print ("the string is a palindrome")
    print (string_to_check)
else:
    print ("the string is not a palindrome")
    
