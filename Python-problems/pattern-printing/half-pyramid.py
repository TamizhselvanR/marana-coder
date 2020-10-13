# i j 01234
# 0       *
# 1      **
# 2     ***
# 3    ****
# 4   *****

n = 5
for i in range(n):
    print(' '*(n-i-1),end = '')
    print('*'*(i+1))
