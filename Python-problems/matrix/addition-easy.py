# Matrix 1
# 1 2 3
# 1 2 3
# 1 2 3

# Matrix 2
# 1 1 1
# 1 1 1
# 1 1 1

# Result
# 2 3 4
# 2 3 4
# 2 3 4

# Matrix addition easy way
mat1 = []
mat2 = []
row = 3
col = 3
for i in range(row):
    temp=list(map(int,input().split(" ")))
    mat1.append(temp)
    
for i in range(row):
    temp=list(map(int,input().split(" ")))
    mat2.append(temp)

mat3 = [[0 for i in range(row)] for i in range(row)]
for i in range(row):
    for j in range(col):
        mat3[i][j] = mat1[i][j] + mat2[i][j]
