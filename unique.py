# given a range for example 105, 109, you have to check whether
# if this range contains unique number or not
#

flag = True
first, last = map(int, input().split(','))
for i in range(first, last):
    s = set(list(str(i)))
    if len(s) != len(list(str(i))):
        flag = False
        print('All elements in given range are not unique')
        break
if(flag == True):
    print('All elements in given range are not unique')




