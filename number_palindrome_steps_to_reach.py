def num_reverse(num):
    lst = [ x for x in str(num)]
    lst1 = lst[::-1]
    new_num = int(''.join((lst1)))
    return new_num

def palindrome_chain_length(n):
    # parameter n is a positive integer # your function should return the number of steps
    done = False
    count = 0
    while done == False:
        if n == num_reverse(n):
            done = True
            return count
        else:
            n = n+num_reverse(n)
            count += 1
            if count > 100:
                return 100
                
