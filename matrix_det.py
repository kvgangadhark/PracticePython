def Print_Matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    print ('rows: '+str(rows)+ 'cols: '+str(cols))
    for each in matrix:
        print(each)
        

def Get_Sub_Matrix(row, col, matrix):
    output = []
    rows = len(matrix)
    cols = len(matrix[0])
    if row >= rows-2:
        return [0]
    print ('requested sub for '+str(row)+'*'+str(col))
    for index in range(row+1, rows):
        #output.append(matrix[index][0:col-1:]+matrix[index][col::])
        lst = matrix[index]
        out1 = []
        for jndex in range(0,len(lst)):
            if jndex != col:
                out1.append(lst[jndex])
        output.append(out1)
    Print_Matrix(output)
    return output

def det(matrix):
    Print_Matrix(matrix)
    sum_d = 0
    rows = len(matrix)
    cols = len(matrix[0])
    if rows == 1 and cols == 1:
        return matrix[0][0]
    if rows == 2 and cols == 2:
        return matrix[0][0]*matrix[1][1] - matrix[0][1]*matrix[1][0]
    for index in range(0,rows-2):
        for jndex in range(0, cols -2):
            if jndex %2 == 0:
                sum_d += det(Get_Sub_Matrix(index, jndex, matrix))
            else:
                sum_d -= det(Get_Sub_Matrix(index, jndex, matrix))
    return sum_d
                
                             
        

matrix1 = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
matrix2 = [[1,2],[-1,3]]
matrix3 = [[1,0,1],[1,1,1],[1,-1,1]]
print (det(matrix1))
##Get_Sub_Matrix(0, 0, matrix1)
##Get_Sub_Matrix(0, 1, matrix1)
##Get_Sub_Matrix(0, 2, matrix1)
##Get_Sub_Matrix(1, 0, matrix1)
##Get_Sub_Matrix(1, 1, matrix1)
##Get_Sub_Matrix(1, 2, matrix1)
##Get_Sub_Matrix(2, 0, matrix1)
##Get_Sub_Matrix(2, 1, matrix1)
##Get_Sub_Matrix(2, 2, matrix1)
