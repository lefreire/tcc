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
sys.path.insert(0, '../configure/')
# from userClass import *
from configure import *
import importlib
import os, subprocess

class Island:
    """ Class to run the optimizer using the island method 
    """
    def __init__(self, dim):
        """ Constructor
        """
        self.dim = dim

    def compileCode(self, individual):
        """ Method to compile the target code
            This method uses methods defined by the user  
        """
        # userClass = userClass()
        module = importlib.import_module(getClass())
        my_class = getattr(module, getClassName())
        userClass = my_class()
        pathCompile = userClass.pathToCompile()
        commandCompile = userClass.argumentsToCompile()
        # print commandCompile
        flags = userClass.initialFlags()
        individual = self.changeFlags(individual, flags)
        commandCompile = commandCompile + " CXXFLAGS="+ individual

        path = os.getcwd()
        os.chdir(pathCompile)
        print "======= Changing directory ======="
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        print commandCompile
        p = subprocess.Popen(commandCompile, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        os.chdir(path)
        print "======= Changing directory ======="
   
    def cleanCode(self):
        """ Method to clean the target code
            This method uses methods defined by the user
            It cleans all the executable files
        """
        # userClass = userClass()
        module = importlib.import_module(getClass())
        my_class = getattr(module, getClassName())
        userClass = my_class()
        path = os.getcwd()
        pathClean = userClass.pathToClean()
        commandClean = userClass.argumentsToClean()

        os.chdir(pathClean)
        print "======= Changing directory ======="
        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        p = subprocess.Popen(commandClean, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        os.chdir(path)
        print "======= Changing directory ======="


    def fitness(self, x):
        """ Method to calculate the fitness value
            This method uses methods defined by the user
            The method name and the return is required for the pygmo structure to work the island method
        """
        # userClass = userClass()
        module = importlib.import_module(getClass())
        my_class = getattr(module, getClassName())
        userClass = my_class()
        self.compileCode(x) 
        y =  userClass.evaluationFunction(x)
        print "evaluation: ", y
        self.cleanCode()
        return [y]


    def get_bounds(self):
        """ Method returns the bound values
            The method name and the return is required for the pygmo structure to work the island method
        """
        return ([1] * self.dim, [6] * self.dim)
 
    def changeFlags(self, individual, options):
        """ Method returns the population with the flags
            In this method, if the bool value is 1, it is switched to the correspondent flag
        """
        individual_def = ""
        for ind in xrange(0, len(individual)):
            print options
            if individual[ind]:
                individual_def = individual_def + " " + options[ind]
        individual_def = '"' + individual_def + '"'
        return individual_def

    def islandMethod(self, population, flag_option):
        """ Method to run the optimizer
        """
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
        plt.savefig('island/graphicChanges/myfig_elitism_'+str(no_generations)+'.png')
        #plt.show()

def main(population, flag_option):
    Island(6).islandMethod(population, flag_option)


if __name__ == "__main__":
    main()
