def get_digits(n):
    lst = []
    while int(n) > 0:
        lst.append(int(n % 10))
        n = int(n) / 10
    lst.sort()
    #print (lst)
    return lst

def next_bigger(n):
    print (n)
    lst =  get_digits(n)
    for x in range(n+1, n*10):
        if get_digits(x) == lst:
            return x
    return -1


def next_bigger1(n):
    lst = get_digits(n)
    k = len(lst)
    for x in range(0, k):
        if lst[k-1-x] > lst[k-2-x]:
            tmp = lst[k-2-x]
            lst[k-2-x] = lst[k-1-x]
            lst[k-1-x] = tmp
            sum = 0
            for each in lst:
                sum += (sum *10) + each
            return sum
        
#get_digits(12)
print (next_bigger(12))
print (next_bigger(123))
print (next_bigger(1234567899))
