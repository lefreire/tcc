#pygmo for island method
import pygmo as pg
import numpy as np
from random import randint
#for graphics
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
#for scientific notation
from decimal import Decimal
#importing class
import sys
sys.path.insert(0, '../framework/')
from test import *

class Island:
    def __init__(self, dim):
        self.dim = dim

    def compileCode(self, individual):
        test = Test()
        pathCompile = test.pathToCompile()
        commandCompile = test.argumentsToCompile()
        print commandCompile
        flags = test.initialFlags()
        individual = self.changeFlags(individual, flags)
        commandCompile = commandCompile + " CXXFLAGS="+ individual

        path = os.getcwd()
        os.chdir(pathCompile)
        print "======= Changing directory ======="
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        p = subprocess.Popen(commandCompile, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        os.chdir(path)
        print "======= Changing directory ======="
   
    def cleanCode(self):
        test = Test()
        path = os.getcwd()
        pathClean = test.pathToClean()
        commandClean = test.argumentsToClean()

        os.chdir(pathClean)
        print "======= Changing directory ======="
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        p = subprocess.Popen(commandClean, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        os.chdir(path)
        print "======= Changing directory ======="


    def fitness(self, x):
        test = Test()
        self.compileCode(x) 
        y =  test.evaluationFunction(x)

        self.cleanCode()
        return [y]


    def get_bounds(self):
        return ([1] * self.dim, [6] * self.dim)
 
    def changeFlags(self, individual, options):
        individual_def = ""
        for ind in xrange(0, len(individual)):
            print options
            if individual[ind]:
                indivual_def = individual_def + " " + options[ind]
        return individual_def

    def islandMethod(self, population, flag_option):
        #defining some numbers
        no_pop = 10
        no_generations = 50
        no_individuals = 6
        #defining my problem
        prob = pg.problem(Island(no_individuals))
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
        plt.savefig('graphicChanges/myfig_elitism_'+str(no_generations)+'.png')
        #plt.show()

def main(population, flag_option):
    Island(6).islandMethod(population, flag_option)


if __name__ == "__main__":
    main()
