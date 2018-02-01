import pygmo as pg
import numpy as np
from random import randint
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#for scientific notation
from decimal import Decimal

#from ../framework/test.py import *
import sys
sys.path.insert(0, '../framework/')
#print sys
from test import *

class my_problem:
    def __init__(self, dim):
        self.dim = dim

    def fitness(self, x):
        #return [-sum(x)]
        x = Test()
        y =  x.evaluationFunction(x)
        return [y]


    def get_bounds(self):
        #return ([1] * self.dim, [100000] * self.dim)
        return ([1] * self.dim, [6] * self.dim)


def main(population):
    print "APENAS UM TESTE: ", population
    #defining some numbers
    no_pop = 10
    no_generations = 50
    no_individuals = 6
    #defining my problem
    prob = pg.problem(my_problem(no_individuals))
    #prob = pg.problem(pg.rosenbrock(dim = 4))
    print prob

    for i in range(0, 1):
        #creating my population
        pop = pg.population(prob)
        print pop
        #generating the individuals
        for i in range(0, no_pop):
            print "ENTREI AQUI"
            #print "pop teste: ", population[i]
            #pop.push_back(x = population[i])
            pop.push_back(x = population[i])
        print "POPULACAO: ", pop

        values = []
        algo = pg.algorithm(pg.sga(gen=no_generations, cr=0.3, m=0.1, selection = "tournament"))
        algo.set_verbosity(1)
        print algo
        pop = algo.evolve(pop)
        logs = algo.extract(pg.sga).get_log() 
        print logs
        #making the plot
        #plt.plot([l[0] for l in logs],[-l[2] for l in logs], linewidth=2.5,  label  = "Pygmo: "+ str('%.2E' % Decimal(-logs[-1][2])))
        #plt.legend(bbox_to_anchor=(0.5, 0), loc=3,
         #      ncol=2, mode="expand", borderaxespad=0.)
        #naming the x and y label and putting the title
        #plt.xlabel('generations')
        #plt.ylabel('best evaluate')
        #plt.title('Generation with: population= ' + str(no_pop)
         #            + ' , number generation= '+ str(no_generations), bbox={'facecolor': '0.8', 'pad': 5})
        #saving the figure
        #plt.savefig('my_fig_problem_'+str(no_generations)+'.png')
        #plt.savefig('graphicChanges/myfig_elitism_'+str(no_generations)+'.png')

if __name__ == "__main__":
    main()
