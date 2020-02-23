arr = [input('1:'), input('2:'), input('3:')]
count = 0
print(arr)
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            count += 1
print(count)
