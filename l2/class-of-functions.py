import numpy as np


class ClassOfFunctions:
    def __init__(self, p_1, p_2, a):
        self.p_1 = p_1
        self.p_2 = p_2
        self.a = a

    def get_value(self, x):
        return self.p_1(x) * np.sin(self.a * x) + self.p_2(x) * np.cos(self.a * x)

    def __add__(self, class_instance):
        return ClassOfFunctions(self.p_1 + class_instance.p_1, self.p_2 + class_instance.p_2, self.a)

    def __sub__(self, class_instance):
        return ClassOfFunctions(self.p_1 - class_instance.p_1, self.p_2 - class_instance.p_2, self.a)

    # return np.polyder(self.p1) * sin(self.a * x) + self.p1 * cos(self.a * x) + np.polyder(self.p2) * cos(self.a * x) - self.p2 * sin(self.a * x)
    def diff(self):
        return ClassOfFunctions(np.polyder(self.p_1) - self.p_2, self.p_1 + np.polyder(self.p_2), self.a)

    def print_in_readable_form(self):
        ClassOfFunctions.print_polynomial(self.p_1.c)
        print 'sin(', self.a, '* x ) +',
        ClassOfFunctions.print_polynomial(self.p_2.c)
        print 'cos(', self.a, '* x )',
        print '\n'

    @staticmethod
    def print_polynomial(c):
        print '(',
        for i in range(len(c)):
            print c[i], '* x ^', len(c) - i - 1,
            if i != len(c) - 1:
                print '+',
            else:
                print ') *',


class1 = ClassOfFunctions(np.poly1d([4, 3, -2, 10]), np.poly1d([1, 2, 3, 4]), 10)
class1.print_in_readable_form()

class2 = ClassOfFunctions(np.poly1d([1, 4, 10]), np.poly1d([3, 4]), 10)
class2.print_in_readable_form()

(class1 + class2).print_in_readable_form()

class1.diff().print_in_readable_form()

print class1.get_value(5)
