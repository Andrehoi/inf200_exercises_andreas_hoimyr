
# -*- coding: utf-8 -*-

__author__ = "Andreas Sandvik Hoimyr"
__email__ = "andrehoi@nmbu.no"


import random


class Walker:

    def __init__(self, samfunnet_position, home_position):
        self.student = samfunnet_position
        self.home = home_position
        self.count_steps = 0

        return

    def move(self):
        """ Moves the student either +1 step or -1 step towards home"""
        step = random.randint(1, 2)
        if step == 2:
            step = -1
        self.student += step

        self.count_steps += 1

        return

    def is_at_home(self):
        """ Checks if student is at home """
        return self.student == self.home

    def get_position(self):
        """ Returns the position of the student"""
        return self.student

    def get_steps(self):
        """Returns the number of steps to reach home"""
        return self.count_steps


class Simulation:

    def __init__(self, samfunnet_position, home_position, seed):
        self.start = samfunnet_position
        self.home = home_position
        self.seed = random.seed(seed)
        """
        Initialise the simulation
        """

    def single_walk(self):
        """
        Simulate single walk from start to home, returning number of steps.

        """

        walker = Walker(self.start, self.home)

        while not walker.is_at_home():
            walker.move()

        return walker.get_steps()

    def run_simulation(self, num_walks):
        """
        Run a set of walks, returns list of number of steps taken.

        """
        walk_list = []
        for _ in range(num_walks):
            walk_list.append(self.single_walk())

        return walk_list


if __name__ == '__main__':

    for _ in range(2):
        simulation_one = Simulation(0, 10, 12345)
        simulation_two = Simulation(10, 0, 12345)
        print(simulation_one.run_simulation(20))
        print(simulation_two.run_simulation(20))

    simulation_three = Simulation(0, 10, 54321)
    simulation_four = Simulation(10, 0, 54321)
    print(simulation_three.run_simulation(20))
    print(simulation_four.run_simulation(20))
