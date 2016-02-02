# Write a function to generate a random password.
# 8 to 15 charaters long, must include one small case, one upper case and one of symbols !@#$%^&*()-+?.

import random

list_small    = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
list_caps     = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
special_chars = ['!','@','#','$','%','^','&','*','(',')','-','+','?']

length = random.randint(8,16)

print(length)

len_sm = random.randint(1,(length/3))
len_cap= random.randint(1,(length/3))
len_sp = random.randint(1,(length/3))

while (len_sm + len_cap + len_sp ) < 8:
    len_sm  += 1
    len_cap += 1
    len_sp  += 1

p_len = (len_sm + len_cap + len_sp )

password= []

while p_len >= 6:
    password.append(list_small[random.randint(0,25)])
    p_len -= 1
                   
while p_len >= 2:
    password.append(list_caps[random.randint(0,25)])
    p_len -= 1
    
while p_len >= 0:
    password.append(special_chars[random.randint(0,len(special_chars)-1)])
    p_len -= 1

print (''.join(password))
                   
