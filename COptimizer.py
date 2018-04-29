from importlib import import_module
from inspect import getmembers, isclass
import random
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
from framework.island.island import main
# from configure.configure import *


class COpt():
    """ Class to run the optimizer 
    """    

    def __init__(self):
        """ Constructor
        """
        module = import_module(sys.argv[1])
        klasses = getmembers(module, isclass)
        my_class = getattr(module, klasses[0][0])
        self.user_class = my_class()

    def initial_parameters(self):
        """ Defining initial parameters to pass to the optimizer 
        """
        args = 5*[0]
        args[0] = 50 #number of generations
        args[1] = 10 # size of population
        args[2] = 6 #size of individual
        args[3] = 0.3 #crossover rate
        args[4] = 0.1 #mutation rate
        return args

    def get_flags(self):
        """ Getting the flag options defined by the user
        """
        return self.user_class.flags_list

    def construct_first_population(self):
        """ Constructing the first population 
            This first population is composed by 0's and 1's, representing if the flag is present in the population or not
        """
        options = self.get_flags()
        no_options = len(options)
        parameters = self.initial_parameters()
        individuos = []
        for ind in xrange(0, parameters[1]):
            individual_first = []
            for individual in xrange(0, no_options):
                individual_first = individual_first + [random.randint(0,1)]
            individuos = individuos + [individual_first]
        return individuos

    def run_optimization(self):
        """ Run the optimizer using the informations above
        """
        population = self.construct_first_population()
        flags = self.get_flags()
        main(self.user_class, population, flags) 
        

if __name__ == "__main__":
    COpt().run_optimization()

# x = COpt()
# print x.get_flags()

