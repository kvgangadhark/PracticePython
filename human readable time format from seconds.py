def format_duration(seconds):
    #your code here
    n = seconds
    str1 = ''
    append = 0
    if n <= 0:
        return 'now'
    if n >= 31536000:
        str1 += 'str(n/31536000) year'
        if n/31536000 > 1:
            str1 += 's'
        n %= 31536000
        append = 1
    if n >= 86400:
        if append == 1:
            str1+=', '
            append = 0
        str1 += str(n/86400)+' day'
        if n/86400 > 1:
            str1 += 's'
        append = 1
        n%=86400
    if n >= 3600:
        if append == 1:
            str1+=', '
            append = 0
        str1 += str(n/3600)+' hour'
        if n/3600 > 1:
            str1 += 's '
        append = 1
        n %=3600
    if n >= 60:
        if append == 1:
            str1+=', '
            append = 0
        str1 += str(n/60)+' minute'
        if n/60 > 1:
            str1 += 's'
        append = 1
        n %= 60
    if n > 0:
        if append == 1:
            str1+=' and '
            append = 0
        str1 += str(n)+' second'
    if n > 1:
        str1 += 's'
    print str1
    return str1
        
    
