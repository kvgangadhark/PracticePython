# variable length banner
# we should print the banner proportianate to the name
# for ex
#-----------
#.::Ganga::.
#-----------
#---------------
#.::Gangadhar::.
#---------------
#instead of 
#
#-----------
#.::KvGangadhar:.
#-----------

def print_banner(name):
    length = len(name) + 6
    print ("-"*length)
    print ()
    print ("-::"+name+"::-")
    print ()
    print ("-"*length)

name = input("enter the name to be printed in banner:")
print_banner(name)
