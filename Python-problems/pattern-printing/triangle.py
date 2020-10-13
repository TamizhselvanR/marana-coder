# i j 012345678
# 0       *
# 1      ***
# 2     *****
# 3    *******
# 4   *********

n = 5
j = 1
for i in range(n):
    print(' '*(n-i-1),end = '')
    print('*'*j)
    j += 2


# *********
#  *******
#   *****
#    ***
#     *

n = 5
j = (n*2) - 1
for i in range(n):
    print(' '*(i),end = '')
    print('*'*j)
    j -= 2
