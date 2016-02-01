
#to_decode = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"

#to_decode = "http://www.pythonchallenge.com/pc/def/map.html"
to_decode = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
def orig_solution():

    index = 0 
    length = len(to_decode)
    new_str = []

    while index < length:
        code = ord(to_decode[index])
        if code in range(65,91) or code in range(97,123):
            if code >=121:
                code -= 24
            elif code >=89 and code < 97:
                code -= 24
            else:
                code +=2
            new_str.append(chr(code))
        else:
            new_str.append(chr(code))
        index += 1

    print("".join(new_str))



orig_solution()


