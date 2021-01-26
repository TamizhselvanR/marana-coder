# Binary to Decimal Conversion

bin = list('10111')
ans = 0
for i in range(len(bin)):
    dig = bin.pop()
    if(dig != '0'):
        ans += pow(2, i)
print(ans)

# Inbuilt Method

print(int('10111', 2))
