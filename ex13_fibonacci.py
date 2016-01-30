#write a number to print the given number of fibonacci numbers

def print_fibo(num):
    series=[1,1]
    len = 2
    if num == 1:
        print (1)
        return
    if num == 2:
        print (1,1)
        return
    while num!=2:
        series.append(int(series[len-2] +series[len-1]))
        len += 1
        num -= 1
    print(series)

n = int(input("how many fibs do u want:"))
print_fibo(n)


        
