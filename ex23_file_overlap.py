with open('primes.txt','r') as f1:
    primes = f1.read()
    f1.close()
with open('happynumbers.txt','r') as f2:
    happynums = f2.read()
    f2.close()
p = (','.split(primes))
result = []
print(p)
for each in p:
    if each != '[' and each != ']' and each != ',' and each !=' ':
        if each in happynums:
            result.append(each)
print(result)
