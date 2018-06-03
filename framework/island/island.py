from decimal import Decimal
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
    def __init__(self, user_class, dim):
        """ Constructor
        """
        self.user_class = user_class
        self.dim = dim
        self.compClean = CompClean(self.user_class)
        self.no_pop = 0
        self.no_generations = 0
        self.no_individuals = 0
        self.crossover_rate = 0
        self.mutation_rate = 0
        self.results = Results(self.user_class)
        self.prob = None

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

        self.prob = pg.problem(Island(self.user_class, 
                               self.no_individuals))
        # #prob = pg.problem(pg.rosenbrock(dim = 4))
        # print prob
   
    def fitness(self, x):
        """ Method to calculate the fitness value
            This method uses methods defined by the user
            The method name and the return is required for the 
            pygmo structure to work the island method
        """
        self.user_class.pre()
        self.compClean.compile_code(x) 
        y =  self.user_class.evaluation_function()
        print "evaluation: ", y
        self.compClean.clean_code()
        self.user_class.pos()
        self.results.set_values_evaluation(y)
        return [self.user_class.min_max*y]

    def get_bounds(self):
        """ Method returns the bound values
            The method name and the return is required for the 
            pygmo structure to work the island method
        """
        return ([0] * self.dim, [1] * self.dim)

    def create_population(self, prob, population):
        pop = pg.population(prob)
        for i in range(0, self.no_pop):
            pop.push_back(x = population[i])
        return pop
 
    def island_method(self, population, flag_option, user_class):
        """ Method to run the optimizer
        """

        #defining my problem
        # prob = pg.problem(Island(user_class, no_individuals))
        # #prob = pg.problem(pg.rosenbrock(dim = 4))
        # print prob

        self.defining_values()
        
        #creating my population
        pop = self.create_population(self.prob, population)
        print "POPULACAO: ", pop
        values = []
        algo = pg.algorithm(pg.sga(gen=self.no_generations, 
                                   cr=self.crossover_rate, 
                                   m=self.mutation_rate, 
                                   selection = "tournament"))
        
        # algo.set_verbosity(1)
        # print algo
        pop = algo.evolve(pop)
        logs = algo.extract(pg.sga).get_log()

        # print "logs: ", logs
        #making the plot
        # plt.plot([l[0] for l in logs],[l[2] for l in logs], 
        #         linewidth=2.5,  
        #         label  = "Pygmo: "+ str('%.2E' % Decimal(-logs[-1][2])))
        # plt.legend(bbox_to_anchor=(0.5, 0), loc=3,
        #        ncol=2, mode="expand", borderaxespad=0.)
        # #naming the x and y label and putting the title
        # plt.xlabel('generations')
        # plt.ylabel('best evaluate')
        # plt.title('Generation with: population= ' + str(self.no_pop) 
        #            + ' , number generation= '+ str(self.no_generations), 
        #             bbox={'facecolor': '0.8', 'pad': 5})
        # #saving the figure
        # plt.savefig('my_fig_problem_'+str(no_generations)+'.png')
        # plt.savefig('framework/island/graphicChanges/myfig_elitism_'
        #             +str(self.no_generations)+'.png')
        # #plt.show()
        # self.results.get_graphic()

def main(user_class, population, flag_option):
    print user_class.flags_list
    island = Island(user_class, 6)
    island.island_method(population, flag_option, user_class)
    print ("teste: ", island.results.def_values_evaluation)
    island.results.get_graphic()


if __name__ == "__main__":
    main()
