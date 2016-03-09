def get_neighbours(cells, i, j):
    output = []
    live = dead = 0
    rows = len(cells)
    cols = len(cells[0])
    x = i-1
    y = j-1
    while x <= i+1:
        while y < j+1:
            if x <= rows and cols <= cols and rows > 0 and cols > 0:
                if cells[x][y] == 1:
                    live += 1
                if cells[x][y] == 0:
                    dead += 1
                y += 1
        x += 1
    output.append(live)
    output.append(dead)
    return output

def next_gen(cells):
    # Uncomment next line for an example output
    cells1 = cells
    for i in cells:
        for j in i:
            out = get_neighbours(cells, i, j)
            live = out[0]
            dead = out[1]
            if cells[i][j] == 1 and live < 2:
                cells1[i][j] = 0
            elif cells[i][j] == 1 and live >=2 and live <=3:
                cells1[i][j] = 1
            elif cells[i][j] == 1 and live > 3:
                cells1[i][j] = 0
            elif cells[i][j] == 0 and live >= 3:
                cells1[i][j] = 1
    return cells1

cells = [[0,1,1,0,1],[0,1,1,0,1],[0,1,1,0,1],[0,1,1,0,1],[0,1,1,0,1]]
