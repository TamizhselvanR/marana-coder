# Given a integer find sum and product of
# all digits

# input = 1234
# sum = 1+2+3+4 = 10
# product = 1*2*3*4 = 24

sum = 0
prod = 1
n = 1234
while(n!=0):
    rem = n % 10
    sum += rem
    prod *= rem
    n = int(n / 10)
print(sum, prod)

sum = 0
n = input()
for i in n:
    sum += int(i)
print(sum)
