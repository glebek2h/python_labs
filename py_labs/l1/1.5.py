import numpy as np

arr = [10, 0, 0, 12, 1, 0, 13, 0]
res = []
while arr:
    item = arr.pop()
    if item != 0:
        res.insert(0, item)
    else:
        res.append(item)

print(res)
