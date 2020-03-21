import numpy as np

from py_labs.l2.poly import Poly


class ClassOfFunctions:
    def __init__(self, p_1, p_2, a):
        self.p_1 = p_1
        self.p_2 = p_2
        self.a = a

    def get_value(self, x):
        return self.p_1.get_value(x) * np.sin(self.a * x) + self.p_2.get_value(x) * np.cos(self.a * x)

    def __add__(self, class_instance):
        if self.a != class_instance.a:
            raise ValueError('param a of class instances is not equal')
        return ClassOfFunctions(self.p_1 + class_instance.p_1, self.p_2 + class_instance.p_2, self.a)

    def __sub__(self, class_instance):
        return ClassOfFunctions(self.p_1 - class_instance.p_1, self.p_2 - class_instance.p_2, self.a)

    def diff(self):
        return ClassOfFunctions(self.p_1.diff() - self.p_2 * self.a, self.p_1 * self.a + self.p_2.diff(), self.a)

    def print_in_readable_form(self):
        self.p_1.print_polynomial(),
        print('sin(', self.a, '* x ) +', end='')
        self.p_2.print_polynomial()
        print('cos(', self.a, '* x )', end='')
        print('\n')


class1 = ClassOfFunctions(Poly([1, 2, 3, -2, 10]), Poly([1, 2, 3, 4]), 10)
print('polynomial_1:')
class1.print_in_readable_form()

class2 = ClassOfFunctions(Poly([1, 4, 10]), Poly([4]), 10)
print('polynomial_2:')
class2.print_in_readable_form()

print('polynomial_1 + polynomial_2:')
(class1 + class2).print_in_readable_form()

print('polynomial_1 - polynomial_2:')
(class1 - class2).print_in_readable_form()

print('(polynomial_1)`:')
print(class1.diff().get_value(2))

print('polynomial_1(2):')
print(class1.get_value(2))


