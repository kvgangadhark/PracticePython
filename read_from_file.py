func = 0
port = 0
shared = 0
qos = 0

with open("sample.txt") as f:
    a = 0
    for line in f:
        a += 1
        lis = line.split()
        x = lis[0]
        if x == "42,":
            func += 1
            
        if x == "41,":
            port += 1
            
        if x == "40,":
            shared+=1
            print(lis[1])
        if x == "44,":
            qos+=1
            
    print("func 41 :"+str(func)+" port: "+str(port)+" shared:"+str(shared)+" qos:"+str(qos))
