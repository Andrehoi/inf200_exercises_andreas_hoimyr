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


class BoundedSimulation(Simulation):

    def __init__(self, samfunnet_position, home_position, seed, left_limit,
                 right_limit):
        super().__init__(samfunnet_position, home_position, seed)

        self.left_limit = left_limit
        self.right_limit = right_limit


if __name__ == '__main__':

