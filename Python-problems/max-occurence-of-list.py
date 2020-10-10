# Given a list = [1,2,3,3,3,1,4,3]

# Output: max = 3, count = 4 times

lis = [1,2,2,3,3,3,1,4,3]
dic = {}
max = lis[0]
count = 1
for i in lis:
    if(not dic.get(i)):
        dic[i] = 1
    else:
        dic[i] += 1
        if(dic[i] > count):
            max = i
            count = dic[i]
print(max, count)