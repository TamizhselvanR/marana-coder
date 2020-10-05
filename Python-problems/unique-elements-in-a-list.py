# Given a list of elements, print all unique 
# elements in the list

# input: [1,2,3,2,1]
# output: [1,2,3]

#code for technical rounds

dic = {}
lis = [1,2,3,2,1]
for i in lis:
    if(not dic.get(i)):
        dic[i] = True
        print(i)

#Alternative method: machine coding round
lis = [1,2,3,2,1]
res = set(lis)
print(res)
