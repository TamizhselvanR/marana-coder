# Matrix 1
# 1 2 3
# 1 2 3
# 1 2 3

# Matrix 2
# 1 1 1
# 1 1 1
# 1 1 1

# Result
# 6 6 6
# 6 6 6
# 6 6 6

# Matrix Mul Efficient way
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

mat3 = []
for i in range(row):
    rows = []
    for j in range(col):
        res = 0
        for k in range(row):
            res += mat1[i][k] * mat2[k][j]
        rows.append(res)
    mat3.append(rows)
print(mat3)