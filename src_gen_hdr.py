#Writing a script which will take a c strucure as input from a file
# and generates c source code that will print each member when mapped
# with binary data.

fields=[]
f1 = open("nic_desc.txt","r")
for eachline in f1:
    lst = eachline.split(" ")
    for each in lst:
        if each == ' ' or each == '' or each == 'u32' or each == "UEXACT16" or each == "UEXACT32":
            lst.remove(each)
    #print (lst)
    fields.append(lst[0])

for each in fields:
    print (each)
    

