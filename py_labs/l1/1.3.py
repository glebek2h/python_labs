a = int(input('1:'))
b = int(input('2:'))

while a != 0 and b != 0:
    if a > b:
        a %= b
    else:
        b %= a
print(a + b)