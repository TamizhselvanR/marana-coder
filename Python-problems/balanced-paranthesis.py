# Given a expression with paranthesis
# find whether it has balanced paranthesis or not(valid or not)
# (() - unbalanced, ()() - balanced

st = '(())())'
stack = []
flag = True
for i in range(len(st)):
    if(st[i] == '('):
    
        stack.append('(')
    elif(st[i] == ')'):
        if(len(stack) == 0 or i == 0):
            flag = False
            break
        else:
            stack.pop()

if((len(stack) == 0) and flag):
    print('balanced')
else:
    print('unbalanced')