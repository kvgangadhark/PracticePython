def encrypt(key, message):
    lst = [x for x in message]
    output = []
    n = 0
    for each in lst:
        n = ord(each)+key
        if ord(each) > 64 and ord(each) < 91:
            if  n > 90:
                n = 65 + n -90
            output.append(chr(n))
        if ord(each) > 96 and ord(each) < 122:
            if n > 121:
                n = 96 + n -121
            output.append(chr(n))
    return "".join(output)

print (encrypt(2,"bucky"))
