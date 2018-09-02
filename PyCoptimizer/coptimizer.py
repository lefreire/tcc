from importlib import import_module
from importlib import import_module
from inspect import getmembers, isclass
import random
import sys
import os
from PyCoptimizer.framework.island import main
from PyCoptimizer.results import Results


class COptimizer(object):
    """ Class to run the optimizer 
    """

    def __init__(self):
        """ Constructor
        Parameters
        ----------
        user_class: class
            Class defined by the user and get in the command line
        results: class
            Class that will show the results at the end
        """
        sys.path.append(os.path.dirname(sys.argv[0]))
        module_name = os.path.splitext(os.path.basename(sys.argv[0]))[0]
        module_user = import_module(module_name)
        sys.path.pop()
        if len(sys.argv) == 2:
            result_path = './'
        else:
            result_path = sys.argv[2]

        result_type = sys.argv[1]
        klasses = getmembers(module_user, isclass)
        my_class = getattr(module_user, klasses[1][0])
        self.user_class = my_class()
        self.results = Results(self.user_class, result_type, result_path)

    def get_flags(self):
        """ Getting the flag options defined by the user

        Returns
        -------
        flags_list: list
            List containing the flags defined by the user
        """
        return self.user_class.flags_list

    def construct_first_population(self):
        """ Constructing the first population 
        This first population is composed by 0's and 1's, 
        representing if the flag is present in the population 
        or not

        Returns
        -------
        individuals: list
            List containing the actived flags in the population
        """
        options = self.get_flags()
        no_pop = self.user_class.dict_optimization["no_pop"]
        individuals = []
        for ind in range(0, no_pop):
            individual_first = []
            for individual in range(0, len(options)):
                individual_first.append(random.randint(0, 1))
            individuals.append(individual_first)
        return individuals

    def run_optimization(self):
        """ Run the optimizer using the informations above
        """
        population = self.construct_first_population()
        flags = self.get_flags()
        main(self.user_class, population, flags, self.results)

    def main(self):
        self.run_optimization()
