def print_cells(cells):
    for each in cells:
        print (each)
    print ('')

cells = [[1,1,0, 1, 0], [0, 1, 0], [0, 1, 0]]
outcells = []

ind = 0
for each in cells:
    outcells.append([])
    for each1 in each:
        outcells[ind].append(0)
    ind += 1

print_cells(cells)
print_cells(outcells)
