# -*- coding: utf-8 -*-


__author__ = 'andreas sadnvik hoimyr'
__email__ = 'andrehoi@nmbu.no'


class LCGRand:

    def __init__(self, seed):
        self.counter = 0
        self.lcg_value = seed
        return

    def rand(self):
        """Returns the value given by formula of random values. The formula
        is constant and does not change.
        source:
        https://github.com/yngvem/INF200-2019-Exercises/blob/master/
        exersices/ex04.rst
        """

        lcg_constant = 7**5
        limit_value = 2**31-1

        self.lcg_value = lcg_constant * self.lcg_value % limit_value
        self.counter += 1

        return self.lcg_value


class ListRand:

    def __init__(self, list_of_numbers):
        self.numbers = list_of_numbers
        self.counter = 0
        return

    def rand(self):
        """ Returns the first number of input list, then second number if
        called twice, and third if called thrice etc."""
        if self.counter > len(self.numbers) - 1:
            raise RuntimeError

        number = self.numbers[self.counter]
        self.counter += 1

        return number


if __name__ == '__main__':

    test_lcg = LCGRand(500)
    print(test_lcg.rand())
    print(test_lcg.rand())
    print(test_lcg.rand())

    test_list_rand = ListRand([1, 2, 3, 4])
    print(test_list_rand.rand())
    print(test_list_rand.rand())
