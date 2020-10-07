# Given a string

# 1. Reverse the String
# 2. Check if a string is a palindrome or not.

st = list('elole')

i = 0
j = len(st) - 1

# Program to reverse

while(i < j):
    temp = st[i]
    st[i] = st[j]
    st[j] = temp
    i += 1
    j -= 1
print(st)

# Program to check if it is a palindrome or not

flag = True
while(i < j):
    if(st[i] != st[j]):
        flag = False
        break
    i += 1
    j -= 1
if(flag):
    print('palindrome')
else:
    print('not')
print(st)
