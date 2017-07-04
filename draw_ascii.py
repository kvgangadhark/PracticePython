import sys
def draw_ascii():
    i = 0
    for i in range(255):
        sys.stdout.write(chr(i)+' ')
        if i%16 == 15:
            sys.stdout.write("\n")
    

draw_ascii()
