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
from framework.pre import Pre
from framework.pos import Pos


class Island:
    """ Class to run the optimizer using the island method 
    """
    def __init__(self, user_class, dim):
        """ Constructor
        """
        self.user_class = user_class
        self.dim = dim
        self.pos = Pos(self.user_class)
        self.pre = Pre(self.user_class)
   
    def fitness(self, x):
        """ Method to calculate the fitness value
            This method uses methods defined by the user
            The method name and the return is required for the pygmo structure to work the island method
        """
        # userClass = userClass()
        self.pre.compile_code(x) 
        y =  self.user_class.evaluation_function()
        print "evaluation: ", y
        self.pos.clean_code()
        return [y]


    def get_bounds(self):
        """ Method returns the bound values
            The method name and the return is required for the pygmo structure to work the island method
        """
        return ([0] * self.dim, [1] * self.dim)
 

    def island_method(self, population, flag_option, user_class):
        """ Method to run the optimizer
        """
        #defining some numbers
        no_pop = 3
        no_generations = 3
        no_individuals = 3
        #defining my problem
        prob = pg.problem(Island(user_class, no_individuals))
        #prob = pg.problem(pg.rosenbrock(dim = 4))
        print prob

        for i in range(0, 1):
            #creating my population
            pop = pg.population(prob)
            print pop
            #generating the individuals
            for i in range(0, no_pop):
                print "ENTREI AQUI"
                #print "pop userClasse: ", population[i]
                #pop.push_back(x = population[i])
                pop.push_back(x = population[i])
        print "POPULACAO: ", pop
        values = []
        algo = pg.algorithm(pg.sga(gen=no_generations, cr=0.3, m=0.1, selection = "tournament"))
        algo.set_verbosity(1)
        print algo
        pop = algo.evolve(pop)
        logs = algo.extract(pg.sga).get_log()
        print "logs: ", logs
        #making the plot
        plt.plot([l[0] for l in logs],[l[2] for l in logs], linewidth=2.5,  label  = "Pygmo: "+ str('%.2E' % Decimal(-logs[-1][2])))
        plt.legend(bbox_to_anchor=(0.5, 0), loc=3,
               ncol=2, mode="expand", borderaxespad=0.)
        #naming the x and y label and putting the title
        plt.xlabel('generations')
        plt.ylabel('best evaluate')
        plt.title('Generation with: population= ' + str(no_pop) 
                      + ' , number generation= '+ str(no_generations), bbox={'facecolor': '0.8', 'pad': 5})
        #saving the figure
        plt.savefig('my_fig_problem_'+str(no_generations)+'.png')
        plt.savefig('framework/island/graphicChanges/myfig_elitism_'+str(no_generations)+'.png')
        #plt.show()

def main(user_class, population, flag_option):
    print user_class.flags_list
    Island(user_class, 6).island_method(population, flag_option, user_class)


if __name__ == "__main__":
    main()
