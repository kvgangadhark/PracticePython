#take a string from the user as input and reverse teh words an print it

orig_str = input("enter the string to be reverse: ")

new_str = orig_str.split(" ")

print (new_str)

n_list= new_str[::-1]

print(n_list)
print(" ".join(n_list))
