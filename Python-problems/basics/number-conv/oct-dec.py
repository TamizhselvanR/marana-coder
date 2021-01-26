# Octal to Decimal Conversion

hex = list('515')
ans = 0
for i in range(len(hex)):
    dig = hex.pop()
    ans += int(dig) * pow(8, i)
print(ans)

# Inbuilt Method

print(int('515', 8))

