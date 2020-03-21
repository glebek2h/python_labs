arr = [4, 7, 6, 9, 2, 1, 99, 33, 12, 13, 17]


def even(x):
    even = []
    for i in range(len(x)):
        if i % 2 == 0:
            even.append(x[i])
    print(even)
    return even


even(arr)
