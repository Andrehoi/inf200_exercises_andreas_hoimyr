# -*- coding: utf-8 -*-


__author__ = 'andreas sandvik hoimyr'
__email__ = 'andrehoi@nmbu.no'

import random


class Walker:

    def __init__(self, samfunnet_position, home_position):
        self.student = samfunnet_position
        self.home = home_position
        self.step = 0
        self.count_steps = 0

        return

    def move(self):
        self.step = random.randint(1, 2)
        if self.step == 2:
            self.step = -1
        self.student += self.step

        self.count_steps += 1

        return

    def is_at_home(self):
        if self.student == self.home:
            return True
        else:
            return False

    def get_position(self):
        return self.student

    def get_steps(self):
        return self.count_steps

if __name__ == '__main__':
    pass