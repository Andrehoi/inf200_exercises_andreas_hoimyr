# -*- coding: utf-8 -*-

__author__ = "Andreas Sandvik Hoimyr"
__email__ = "andrehoi@nmbu.no"


class RandIter:

    def __init__(self, random_number_generator, length):

        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None
        return

    def __iter__(self):
        pass

    def __next__(self):
        pass


class LCGRand:

    def __init__(self, seed):
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

        return self.lcg_value

    def random_sequence(self, length):
        return RandIter(self, length)

    def infinite_random_sequence(self):
        pass
