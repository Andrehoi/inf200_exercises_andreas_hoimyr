# -*- coding: utf-8 -*-

__author__ = "Andreas Sandvik Hoimyr"
__email__ = "andrehoi@nmbu.no"


class RandIter:

    def __init__(self, random_number_generator, length):

        self.generator = random_number_generator
        self.length = length
        self.num_generated_numbers = None

    def __iter__(self):
        """
        Initialise the iterator.

        Returns
        -------
        self : RandIter

        Raises
        ------
        RuntimeError
            If iter is called twice on the same RandIter object.
        """
        if self.num_generated_numbers is not None:
            raise RuntimeError

        self.num_generated_numbers = 0
        return self

    def __next__(self):
        """
        Generate the next random number.

        Returns
        -------
        int
            A random number.

        Raises
        ------
        RuntimeError
            If the ``__next__`` method is called before ``__iter__``.
        StopIteration
            If ``self.length`` random numbers are generated.
        """
        if self.num_generated_numbers is None:
            raise RuntimeError

        if self.num_generated_numbers == self.length:
            raise StopIteration

        self.num_generated_numbers += 1

        return self.generator.rand()


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
        """
        Generate an infinite sequence of random numbers.

        Yields
        ------
        int
            A random number.
        """
        while True:
            yield self.rand()


if __name__ == '__main__':

    generator = LCGRand(1)
    for rand in generator.random_sequence(10):
        print(rand)

    i = 0
    while i < 100:
        rand = generator.infinite_random_sequence()
        print(f'The {i}-th random number is {next(rand)}')

        i += 1
