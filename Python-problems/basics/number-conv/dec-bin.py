# Decimal To binary conversion
# Normal Method

num = 23
value = ''
while(num):
    rem = num % 2
    value += str(rem)
    num = num // 2
print(value[::-1]) # 10111

# Recusrsive method

def binary(num):
    if(num):
        rem = num % 2
        binary(num // 2)
        print(rem, end='')
binary(23) # 10111

# Inbuilt Method

print(bin(23)) # 0b10111

