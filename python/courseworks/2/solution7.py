def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(n):
            if j>i:
                matrix[i][j],matrix[j][i]=matrix[j][i], matrix[i][j]

    for row in matrix:
        row[:]=row[::-1]
    
    return matrix

matrix1=[[1,2,3],[4,5,6],[7,8,9]]
print(rotate(matrix1))

matrix2=[[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
print(rotate(matrix2))