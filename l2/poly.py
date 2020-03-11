import copy


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
        print '(',
        for i in range(len(c)):
            print c[i],
            if i != len(c) - 1:
                print '* x ^', len(c) - i - 1, '+',
            else:
                print ')',

    def __add__(self, class_instance):
        return Poly(Poly.sum_min_arr(self.c, class_instance.c, 'sum'))

    def __sub__(self, class_instance):
        return Poly(Poly.sum_min_arr(self.c, class_instance.c, 'min'))

    def __mul__(self, number):
        return Poly(map(lambda x: x * number, self.c))

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