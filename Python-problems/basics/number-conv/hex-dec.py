# Hexadecimal to Decimal Conversion

hex = list('6D')
ans = 0
for i in range(len(hex)):
    dig = hex.pop()
    if(ord(dig) >= 65):
        dig = ord(dig) - 55
    ans += int(dig) * pow(16, i)
print(ans)

# Inbuilt Method

print(int('6D', 16))