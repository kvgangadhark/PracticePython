#Task

#You are given a string s. Every letter in s appears once.

#Consider all strings formed by rearranging the letters in s.
#After ordering these strings in dictionary order, return the middle term.
#(If the sequence has a even length n, define its middle term to be the
#(n/2)th term.)

def middle_perm(string):
    #list(string).sort
        l = list(string)
        l.sort()
        print(l)
    


middle_perm("ganga")
