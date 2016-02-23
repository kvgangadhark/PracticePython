#Write a program which will find all such numbers 
#which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).

orig_list = [x for x in range(2000,3201)]
#print (orig_list)
new = []

for each in orig_list:
    if each % 7 == 0 and each % 5 != 0:
        new.append(each)
print (new)
