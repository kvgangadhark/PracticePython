#write a function which takes a list of 3 lists each with 3 numbers as input and checks if it has a winner.

def game_checker(l):
    for i in range(0,3):
        if l[i][0] == l[i][1] and l[i][2] == l[i][0]:
            return l[i][0]
    for i in range(0,3):
        if l[0][i] == l[1][i] and l[2][i] == l[0][i]:
            return l[0][i]
    if l[0][0] == l[1][1] and l[1][1] == l[2][2]:
        return l[0][0]
    if l[0][2] == l[1][1] and l[2][0] == l[1][1]:
        return l[0][2]
    return 0

def update_board(l,x,y,c):
    l[x][y]=c


def draw_board(l):

    print (" --- --- ---")
    print ("| "+str(l[0][0])+" | "+str(l[0][1])+" | "+str(l[0][2])+" |")
    print (" --- --- ---")
    print ("| "+str(l[1][0])+" | "+str(l[1][1])+" | "+str(l[1][2])+" |")
    print (" --- --- ---")
    print ("| "+str(l[2][0])+" | "+str(l[2][1])+" | "+str(l[2][2])+" |")
    print (" --- --- ---")

def swap_player(player):
    if player == 1:
        return 2
    elif player == 2:
        return 1

l = [[0,0,0],[0,0,0],[0,0,0]]
draw_board(l)
ret = 0
player = 1
while (ret == 0):
    x = int(input(str(player)+" enter the x coordinate: "))
    if x > 3:
        print("wrong input lost your chance")
        player = swap_player(player)
        continue
    y = int(input(str(player)+" enter the y coordinate: "))
    if y > 3:
        print("wrong input lost your chance")
        continue
    update_board(l,x,y,player)
    draw_board(l)
    player = swap_player(player)
    ret = game_checker(l)

print(str(ret)+"is the winner!")

