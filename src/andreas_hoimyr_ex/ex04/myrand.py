# -*- coding: utf-8 -*-


__author__ = 'andreas sadnvik hoimyr'
__email__ = 'andrehoi@nmbu.no'


class LCGRand:

    def __init__(self, seed):
        self.counter = 0
        self.lcg_list = [seed]
        return

    def rand(self):

        self.lcg_list.append(0)

        lcg_constant = 7**5
        limit_value = 2**31-1

        self.lcg_list[self.counter + 1] = lcg_constant * self.lcg_list[
            self.counter] % limit_value

        self.counter += 1

        return self.lcg_list[self.counter]


a = LCGRand(348)
print(a.rand())
print(a.rand())

class ListRand:

    def __init__(self):
        pass

    def rand(self):
        pass

