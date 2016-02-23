def high_and_low(numbers):
    # ...
    nums = [ int(x) for x in numbers.split(' ') ]
    print (nums)
    smallest = 0
    largest = 0
    for each in nums:
        if each > largest:
            largest = each
        if each < smallest:
            smallest = each
    outPut = []
    outPut.append(smallest)
    outPut.append(largest)
    print (outPut)
    print (''.join(outPut))
    

high_and_low("12 23 34 45 56 67 78 9 1 2 3 4 0 -1")
