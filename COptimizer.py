from importlib import import_module
from inspect import getmembers, isclass
import random
import sys
sys.path.insert(0, '/usr/local/lib/python2.7/site-packages')
from framework.island.island import main


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

    def get_flags(self):
        """ Getting the flag options defined by the user
        """
        return self.user_class.flags_list

    def construct_first_population(self):
        """ Constructing the first population 
            This first population is composed by 0's and 1's, 
            representing if the flag is present in the population 
            or not
        """
        options = self.get_flags()
        no_ind = self.user_class.dict_optimization["individual_size"]
        no_pop = self.user_class.dict_optimization["no_pop"]
        individuos = []
        for ind in xrange(0, no_pop):
            individual_first = []
            for individual in xrange(0, no_ind):
                individual_first.append(random.randint(0,1))
            individuos.append(individual_first)
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
# print x.initial_parameters()

