

def decode(st1):
    str1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    str2 = "cdefghijklmnopqrstuvwxyzabCDEFGHIJKLMNOPQRSTUVWXYZAB"
    e = [x for x in str1]
    d = [x for x in str2]

    i = [x for x in st1]
    o = []

    for each in i:
        if each in e:
            o.append(d[e.index(each)])
        else:
            o.append(each)

    return "".join(o)

original_string = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj"
print (decode(original_string))

print (decode("http://www.pythonchallenge.com/pc/def/map.html"))
