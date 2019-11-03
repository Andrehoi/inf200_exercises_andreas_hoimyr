# -*- coding: utf-8 -*-

__author__ = "Andreas Sandvik Hoimyr"
__email__ = "andrehoi@nmbu.no"


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
