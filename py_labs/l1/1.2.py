x = int(input('1:'))
y = int(input('2:'))
z = x + x/10
count = 1
while z <= y:
    z = z + z/10
    count += 1
print(count)