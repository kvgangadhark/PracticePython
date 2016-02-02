# write a function implementing binary search on a sorted array.

sorted_list = [0,1,2,3,4,5,6,7,8,9,10]

def binary_search(element):
    start = 0
    end   = len(sorted_list)
    search_done = False
    position = -1

    while search_done != True:
        mid = int((end + start) / 2)
        if element == sorted_list[mid]:
            print ("start is "+ str(start)+"mid is "+str(mid)+"end is "+str(end)+"mid has value"+str(sorted_list[mid]))
            search_done = True
            position = mid
        if start == mid:
            print ("start is "+ str(start)+"mid is "+str(mid)+"end is "+str(end)+"mid has value"+str(sorted_list[mid]))
            position = -1
            search_done = True
        elif element > sorted_list[mid]:
            print ("start is "+ str(start)+"mid is "+str(mid)+"end is "+str(end)+"mid has value"+str(sorted_list[mid]))
            start = mid
        elif element < sorted_list[mid]:
            print ("start is "+ str(start)+"mid is "+str(mid)+"end is "+str(end)+"mid has value"+str(sorted_list[mid]))
            end = mid
    return position

inp = int(input("enter the number to search: " ))
print (binary_search(inp))



