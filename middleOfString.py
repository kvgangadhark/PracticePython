def get_middle(s):
    #your code here
    lst = list(s)
    x = len(lst)
    y = int (x/2)
    print (y)
    
    if x % 2 == 0:
        print("even")
        print(lst[y-1:y+2])
    else:
        print("odd")
        print(lst[y-1:y+1])
    

get_middle("123456")
get_middle("ab")
get_middle("abc")
get_middle("abcd")
get_middle("abcde")

