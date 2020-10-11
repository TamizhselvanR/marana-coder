# Binary Search in Python

arr = [ 2, 3, 4, 10, 11, 40 ]
low = 0
x = 1
ans = False
high = len(arr) - 1
while(low <= high):
    mid = (low + high)//2
    print(low,high,mid)
    if(x < arr[mid]):
        high = mid - 1
    elif(x > arr[mid]):
        low = mid + 1
    else:
        ans = mid
        break
if(ans):
    print(ans)
else:
    print('Element not Found')