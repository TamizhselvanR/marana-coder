# Decimal To Octal conversion
# Normal Method

num = 23
value = ''
while(num):
    rem = num % 8
    value += str(rem)
    num = num // 8
print(value[::-1]) # 27

# Recusrsive method

def octa(num):
    if(num):
        rem = num % 8
        octa(num // 8)
        print(rem, end='')
octa(23) # 27

# Inbuilt Method

print(oct(23)) # 0o27

