#   j 01234
# i
# 0   *****
# 1   *   *
# 2   *   *
# 3   *   *
# 4   *****

n = 5
for i in range(n):
    for j in range(n):
        if(i == 0 or i == n-1 or j == 0 or j == n-1):
            print('*',end = '')
        else:
            print(' ',end = '')
    print('')
