# -*- coding: utf-8 -*-

__author__ = "Andreas Sandvik Hoimyr"
__email__ = "andrehoi@nmbu.no"

from walker_sim import Walker
from walker_sim import Simulation
import random


class BoundedWalker(Walker):

    def __init__(self, samfunnet_postition, home_position, left_limit,
                 right_limit):
        super().__init__(samfunnet_postition, home_position)
        self.student = samfunnet_postition
        self.left_limit = left_limit
        self.right_limit = right_limit

    def bounded_move(self):
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

        self.left = left_limit
        self.right = right_limit

    def bounded_sims(self, num_sims):

        walker = BoundedWalker(self.start, self.home, self.left, self.right)

        while not walker.is_at_home():
            walker.bounded_move()

        return walker.get_steps()

    def run_bounded_sims(self, num_walks):

        walk_list = []
        for _ in range(num_walks):
            walk_list.append(self.bounded_sims(num_walks))

        return walk_list


if __name__ == '__main__':

    left_boundary = [0, -10, -100, -1000, -10000]
    seed = 0

    for boundary in left_boundary:
        bound_sim = BoundedSimulation(0, 20, seed, boundary, 20)
        print(" Left boundary {0} with these results:". format(boundary),
              bound_sim.run_bounded_sims(20))
