# Getting matrix as input

# Matrix 1
# 1 2 3
# 1 2 3
# 1 2 3

# Matrix 2
# 1 1 1
# 1 1 1
# 1 1 1

mat1 = []
mat2 = []
row = 3
col = 3
for i in range(rows):
    temp=list(map(int,input().split(" ")))
    mat1.append(temp)
    
for i in range(rows):
    temp=list(map(int,input().split(" ")))
    mat2.append(temp)

# mat1 will be like [[1,2,3],[1,2,3],[1,2,3]]
