import random
#importing method
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
from framework.island.island import *
#importing user methods
from configure.configure import *
import importlib


class COpt():
    """ Class to run the optimizer 
    """    

    def __init__(self):
        """ Constructor
        """
        pass

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

    def get_flag_options(self):
        """ Getting the flag options defined by the user
        """
        # test = Test()
        module = importlib.import_module('framework.'+get_class())
        print module
        my_class = getattr(module, get_class_name())
        userClass = my_class()
        return userClass.initial_flags()

    def construct_first_population(self):
        """ Constructing the first population 
            This first population is composed by 0's and 1's, representing if the flag is present in the population or not
        """
        options = self.get_flag_options()
        no_options = len(options)
        parameters = self.initial_parameters()
        individuos = []
        for ind in xrange(0, parameters[1]):
            individual_first = []
            for individual in xrange(0, no_options):
                #individual_bool = random.randint(0,1)
                individual_first = individual_first + [random.randint(0,1)]
            individuos = individuos + [individual_first]
        return individuos

    def run_optimization(self):
        """ Run the optimizer using the informations above
        """
        population = self.construct_first_population()
        flags = self.get_flag_options()
        main(population, flags) 
        

if __name__ == "__main__":
    COpt().run_optimization()
