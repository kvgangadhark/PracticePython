def get_sorted_word(word):
    clist = [ord(x) for x in word]
    clist.sort()
    clist1 = [chr(x) for x in clist]
    return ''.join((clist1))
    
def anagrams(word, words):
    output = []
    anag1 = get_sorted_word(word)
    for each in words:
        if anag1 == get_sorted_word(each):
            output.append(each)
    return output 
