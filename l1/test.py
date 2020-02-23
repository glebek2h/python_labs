arr = [4, 7, 6, 9, 2]
sum = 0
for i in range(min(arr),max(arr),1):
    if not i in arr:
        sum += i
