def iteration(b, c):
    r = c[0] * b[0]
    for i in range(1, len(b)):
        r = int(r != c[i] * b[i])

    for i in range(len(b) - 1):
        b[i] = b[i + 1]

    b[-1] = r
    return b


def get_sequence(n, a, c):
    res = []
    b = a
    for i in range(n):
        res.append(b[0])
        b = iteration(a, c)
    return res


def lfsr(a, c):
    b = iteration(a, c)
    p = 0
    map_sequence_period = []
    result_sequence = []
    while b not in map_sequence_period:
        result_sequence.append(b[0])
        map_sequence_period.append(b.copy())
        b = iteration(b, c)
        p += 1
    return p, result_sequence


def geffe_generator(n, sequence_1, sequence_2, sequence_3):
    y = []
    for i in range(n):
        s1 = int(sequence_1[i] != sequence_2[i])
        s2 = int(((sequence_1[i] + 1) % 2) != sequence_3[i])
        y.append((s1 + s2) % 2)
    return y


def r(geffe_sequence, i):
    res = 0
    for j in range(len(geffe_sequence) - i):
        res += (-1) ** ((geffe_sequence[j] + geffe_sequence[j + i]) % 2)
    return res


a_1 = [0, 0, 1, 0, 0]
c_1 = [0, 1, 1, 1, 1]
period_1, sequence_1 = lfsr(a_1, c_1)
print('period_1:', period_1)
print('lfsr_1:', sequence_1)

a_2 = [1, 0, 1, 0, 1, 1, 1]
c_2 = [1, 0, 1, 0, 0, 0, 1]
period_2, sequence_2 = lfsr(a_2, c_2)
print('period_2:', period_2)
print('lfsr_2:', sequence_2)

a_3 = [0, 0, 1, 0, 1, 1, 0, 0]
c_3 = [1, 1, 1, 1, 0, 1, 0, 1]
period_3, sequence_3 = lfsr(a_3, c_3)
print('period_3:', period_3)
print('lfsr_3:', sequence_3)

n = 10000
geffe_sequence = geffe_generator(n, get_sequence(n, a_1, c_1), get_sequence(n, a_2, c_2), get_sequence(n, a_3, c_3))
print('geffe:', geffe_sequence)

print('count zeros:', len([x for x in geffe_sequence if x == 0]))
print('count ones:', len([x for x in geffe_sequence if x == 1]))
for i in range(1, 6):
    print('r', i, ':', r(geffe_sequence, i))
