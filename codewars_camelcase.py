def to_camel_case(text):
    output  = []
    lst = [x for x in text]
    needup = False
    for each in lst:
        if each not in ['-', '_']:
            if needup == True:
                output.append(each.upper())
            else:
                output.append(each)
            needup = False
        else:
            needup = True
    return ''.join(output)
