# Decimal To Hexadecimal conversion
# Normal Method

num = 231
ans = ''
while(num):
    rem = num % 16
    value = chr(55 + rem) if rem > 9 else str(rem)
    num = num // 16
    ans += value
print(ans[::-1]) # E7

# Recusrsive method

def hexa(num):
    if(num):
        rem = num % 16
        value = chr(55 + rem) if rem > 9 else str(rem)
        hexa(num // 16)
        print(value, end='')
hexa(231) # E7

# Inbuilt Method

print(hex(231)) # 0xe7