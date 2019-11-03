# -*- coding: utf-8 -*-

__author__ = "Andreas Sandvik Hoimyr"
__email__ = "andrehoi@nmbu.no"

from walker_sim import Walker
from walker_sim import Simulation


class BoundedWalker(Walker):

    def __init__(self, samfunnet_postition, home_position, left_limit,
                 right_limit):
        super().__init__(samfunnet_postition, home_position)

        self.left_limit = left_limit
        self.right_limit = right_limit

    def Bounded(self):
        """ Moves the student either +1 step or -1 step towards home"""
        step = random.randint(1, 2)
        if step == 2:
            step = -1
        self.student += step
        if self.student < self.left_limit:
            self.student = self.left_limit

        if self.student > self.right_limit:
            self.student = self.right_limit

        self.count_steps += 1

        return



class BoundedSimulation(Simulation):

    def __init__(self, samfunnet_position, home_position, seed, left_limit,
                 right_limit):
        super().__init__(samfunnet_position, home_position, seed)

        self.left_limit = left_limit
        self.right_limit = right_limit


    def bounded_run(self):
        pass