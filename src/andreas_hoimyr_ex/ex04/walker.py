# -*- coding: utf-8 -*-


__author__ = 'andreas sandvik hoimyr'
__email__ = 'andrehoi@nmbu.no'

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
        if self.student == self.home:
            return True
        else:
            return False

    def get_position(self):
        """ Returns the position of the student"""
        return self.student

    def get_steps(self):
        """Returns the number of steps to reach home"""
        return self.count_steps


if __name__ == '__main__':

    progress_home = [1, 2, 5, 10, 20, 50, 100]

    for distance in progress_home:

        distance_moved = []

        for _ in range(5):

            walker = Walker(0, distance)

            while not walker.is_at_home():

                walker.move()

            distance_moved.append(walker.get_steps())

        print(' Distance:   {0} -> path lengths:    {1}'.format(
            distance, distance_moved))
