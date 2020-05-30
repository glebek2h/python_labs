import numpy as np


def tau(x):
    return (-1) ** x


def r(nums, i):
    sums = 0
    for j in range(len(nums) - i):
        sums += tau((nums[j] + nums[j + i]) % 2)
    return sums


class LFSR:
    def __init__(self, a, c):
        self.b = np.array(a)
        self.c = np.array(c)
        self.period = self._get_period()

    def _LFSR_iter(self):
        r = np.dot(self.b, self.c) % 2
        for i in range(len(self.b) - 1):
            self.b[i] = self.b[i + 1]
        self.b[-1] = r

    def get_bits(self, n=1):
        bits = np.zeros(n)
        for i in range(n):
            bits[i] = self.b[0]
            self._LFSR_iter()
        return bits

    def _get_period(self):
        tmp = self.b.copy()
        self._LFSR_iter()
        period = 0
        dct = {}
        while tuple(self.b) not in dct:
            dct[tuple(self.b)] = period
            self._LFSR_iter()
            period += 1
        ans = period - dct[tuple(self.b)]
        self.b = tmp
        return ans


class Geffe_gen:
    def __init__(self, lfsr1, lfsr2, lfsr3):
        self.lfsr1 = lfsr1
        self.lfsr2 = lfsr2
        self.lfsr3 = lfsr3

    def get_bits(self, n=1):
        mas1 = self.lfsr1.get_bits(n)
        mas2 = self.lfsr2.get_bits(n)
        mas3 = self.lfsr3.get_bits(n)
        print(mas1, mas2, mas3)
        return (mas1 * mas2) + (mas1 + np.ones(n)) * (mas3) % 2

    def _get_period(self):
        tmp = self.b.copy()
        self._LFSR_iter()
        period = 0
        dct = {}
        while tuple(self.b) not in dct:
            dct[tuple(self.b)] = period
            self._LFSR_iter()
            period += 1
        ans = period - dct[tuple(self.b)]
        self.b = tmp
        return ans


# a1 = [0, 1, 1, 1, 0]
# c1 = [1, 1, 1, 0, 1]
a1 = [0, 0, 1, 0, 0]
c1 = [0, 1, 1, 1, 1]
lfsr1 = LFSR(a1, c1)
print(len(lfsr1.get_bits(lfsr1.period)))
print(f'LFSR1:\n период равен {lfsr1.period}\n последовательность до начала зацикливания{lfsr1.get_bits(lfsr1.period)}')
# a2 = [1, 1, 1, 0, 1, 0, 1]
# c2 = [0, 0, 1, 1, 0, 1, 1]
a2 = [1, 0, 1, 0, 1, 1, 1]
c2 = [1, 0, 1, 0, 0, 0, 1]
lfsr2 = LFSR(a2, c2)
print(f'LFSR2:\n период равен {lfsr2.period}\n последовательность до начала зацикливания{lfsr2.get_bits(lfsr2.period)}')
# a3 = [0, 1, 1, 1, 1, 1, 1, 0]
# c3 = [1, 0, 1, 0, 1, 1, 1, 1]
a3 = [0, 0, 1, 0, 1, 1, 0, 0]
c3 = [1, 1, 1, 1, 0, 1, 0, 1]
lfsr3 = LFSR(a3, c3)
print(f'LFSR3:\n период равен {lfsr3.period}\n последовательность до начала зацикливания{lfsr3.get_bits(lfsr3.period)}')

geffe_gen = Geffe_gen(lfsr1, lfsr2, lfsr3)
numbers = geffe_gen.get_bits(10000)
print('geffe', numbers)

print(f'количество 1: {sum(numbers)}')
print(f'количество 0: {len(numbers) - sum(numbers)}')
for i in range(1, 6):
    print(f'r_{i}: {r(numbers, i)}')