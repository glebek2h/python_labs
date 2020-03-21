import copy
import numbers


class Poly:

    def __init__(self, c):
        self.c = c

    def get_value(self, x):
        s = 0
        for i in range(len(self.c)):
            s += self.c[i] * (x ** (len(self.c) - i - 1))
        return s

    def diff(self):
        c = copy.deepcopy(self.c)
        c.pop()
        for i in range(len(c)):
            c[i] = c[i] * (len(c) - i)
        return Poly(c)

    def print_polynomial(self):
        c = self.c
        print('(', end='')
        for i in range(len(c)):
            print(c[i], end='')
            if i != len(c) - 1:
                print('* x ^', len(c) - i - 1, '+', end='')
            else:
                print(')', end='')

    def __add__(self, class_instance):
        return Poly(Poly.sum_min_arr(self.c, class_instance.c, 'sum'))

    def __sub__(self, class_instance):
        return Poly(Poly.sum_min_arr(self.c, class_instance.c, 'min'))

    def __mul__(self, number):
        if isinstance(number, numbers.Number):
            return Poly(list(map(lambda x: x * number, self.c)))
        elif isinstance(number, Poly):
            a = self.c
            b = number.c
            poly_arr = []
            for i in range(len(a)):
                c = []
                for k in range(0, len(a) * len(b)):
                    c.append('None')
                pow_a = len(a) - i - 1
                max_pow = 0
                for j in range(len(b)):
                    pow_b = len(b) - j - 1
                    if (pow_a + pow_b) > max_pow:
                        max_pow = pow_a + pow_b
                    if c[pow_a + pow_b] is 'None':
                        c[pow_a + pow_b] = a[i] * b[j]
                    else:
                        c[pow_a + pow_b] = c[i] + a[i] * b[j]
                poly_arr.append(Poly([0 if x == 'None' else x for x in c[:max_pow + 1][::-1]]))
            for i in range(1, len(poly_arr)):
                poly_arr[0] += poly_arr[i]
            return poly_arr[0]

    @staticmethod
    def sum_min_arr(a, b, sum_or_min):
        if len(a) < len(b):
            if len(a) == 1:
                b_copy = [b[len(b) - 1]]
            else:
                b_copy = b[len(b) - len(a):]
            return b[:len(b) - len(a)] + Poly.add(a, b_copy) if sum_or_min == 'sum' else b[:len(b) - len(a)] + Poly.min(
                a, b_copy)
        else:
            if len(b) == 1:
                a_copy = [a[len(a) - 1]]
            else:
                a_copy = a[len(a) - len(b):]
            return a[:len(a) - len(b)] + Poly.add(a_copy, b) if sum_or_min == 'sum' else a[:len(a) - len(b)] + Poly.min(
                a_copy, b)

    @staticmethod
    def add(a, b):
        return list(map(lambda x, y: (x or 0) + (y or 0), a, b))

    @staticmethod
    def min(a, b):
        return list(map(lambda x, y: (x or 0) - (y or 0), a, b))


p1 = Poly([1, 0, 0, 2, 3, 4])
p2 = Poly([1, 2, 1])
p1.print_polynomial()
print('')
p2.print_polynomial()
(p1 * p2).print_polynomial()
print('\n', (p1 * p2).get_value(5))
p1 = Poly([1, 0, 2])
p2 = Poly([1, 0, -1])
(p1 - p2).print_polynomial()