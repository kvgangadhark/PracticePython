def pascal_case(string):
    lst = [x for x in string]
    output = []
    firstone = True
    for each in lst:
        if ord(each) < 97 and ord(each) > 65:
            if firstone == False:
                output.append('_')
        else:
            firstone = False
        output.append(each)
##        output.append(each.lower())  #Incase you need to convert every thign to lower case 
    return "".join(output)

print (pascal_case("TestSetUp"))
