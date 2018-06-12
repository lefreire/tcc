from decimal import Decimal
from math import fmod
from importlib import import_module
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import os
import pygmo as pg
from random import randint
import subprocess
import sys
from framework.compClean import CompClean
from src.results import Results


class Island:
    """ Class to run the optimizer using the island method 
    """
    def __init__(self, user_class, population):
        """ Constructor
        """
        self.user_class = user_class
        self.dim = self.user_class.dict_optimization['individual_size']
        self.compClean = CompClean(self.user_class)
        self.no_pop = 0
        self.no_generations = 0
        self.no_individuals = 0
        self.crossover_rate = 0
        self.mutation_rate = 0
        self.population = population
        self.prob = None
        self.pop = None

    def defining_values(self):
        self.no_pop = self.user_class.dict_optimization["no_pop"]
        self.no_generations = self.user_class.\
                              dict_optimization["no_generations"]
        self.no_individuals = self.user_class.\
                              dict_optimization["individual_size"]
        self.crossover_rate = self.user_class.\
                              dict_optimization["crossover_rate"]
        self.mutation_rate = self.user_class.\
                             dict_optimization["mutation_rate"]
        self.prob = pg.problem(self)
       
    def fitness(self, x):
        """ Method to calculate the fitness value
            This method uses methods defined by the user
            The method name and the return is required for the 
            pygmo structure to work the island method
        """
        self.user_class.pre()
        self.compClean.compile_code(x) 
        y =  self.user_class.evaluation_function()
        self.compClean.clean_code()
        self.user_class.pos()
        return [self.user_class.min_max*y]

    def get_bounds(self):
        """ Method returns the bound values
            The method name and the return is required for the 
            pygmo structure to work the island method
        """
        return ([0] * self.dim, [1] * self.dim)

    def create_population(self, prob, population):
        """ Method to set the population
        """
        pop = pg.population(prob)
        for i in range(0, self.no_pop):
            pop.push_back(x = population[i])
        return pop
 
    def island_method(self, population, flag_option, user_class):
        """ Method to run the optimizer
        """
        self.defining_values()
        self.pop = self.create_population(self.prob, self.population) 
        
        algo = pg.algorithm(pg.sga(gen=self.no_generations, 
                                   cr=self.crossover_rate, 
                                   m=self.mutation_rate, 
                                   selection = "tournament"))
        
        algo.set_verbosity(2)
        self.pop = algo.evolve(self.pop)
        logs = algo.extract(pg.sga).get_log()


def main(user_class, population, flag_option):
    island = Island(user_class, population)
    island.island_method(population, flag_option, user_class)
    print(user_class.flags_list)


if __name__ == "__main__":
    main()
