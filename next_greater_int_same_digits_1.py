def next_bigger(n):
    #your code here
    lst1 = []
    #n = 513
    print (n)
    orig = n
    while n>0:
        lst1.append(int(n%10))
        n =int(n / 10)
    lst = lst1[::-1]
    print (lst)
    k = len(lst)
    for x in range(0,len(lst)):
        if lst[k-x-1] < 9:
            tmp = lst[len(lst)-x-1]
            print ('tmp is '+str(tmp)+' x is '+str(x))
            break
    for y in range(x+1,k):
        if lst[k-y-1] == tmp:
            x = y
        if lst[k-y-1] < tmp:
            print(22)
            z = lst[k-y-1]
            print(24)
            lst[k-y-1] = tmp
            print(26)
            lst[k-x-1] = z
            print(28)
            break
    print (lst)
    sum = 0
    for each in lst:
        sum = 10*sum+each
    print (sum)
    return sum
    
next_bigger(123456879)
