#open the chars file and read unique characters from it.


f = open("chars.txt")

str1 = f.read()

#print (str1)
l = [x for x in str1]
o = []

for each in l:
    if each not in o:
        o.append(each)

print (o)        

