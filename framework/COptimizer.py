import random
#importing method
import sys
sys.path.insert(0, '../island/')
from my_problem import *
#importing user methods
from test import *

class COpt():
    
    def __init__(self):
        pass

    def initialParameters(self):
        args = 5*[0]
        args[0] = 50 #number of generations
        args[1] = 10 # size of population
        args[2] = 6 #size of individual
        args[3] = 0.3 #crossover rate
        args[4] = 0.1 #mutation rate
        return args

    def getFlagOptions(self):
        test = Test()
        return test.initialFlags()

    def constructFirstPopulation(self):
        options = self.getFlagOptions()
        no_options = len(options)
        parameters = self.initialParameters()
        individuos = []
        for ind in xrange(0, parameters[1]):
            individual_first = []
            for individual in xrange(0, no_options):
                #individual_bool = random.randint(0,1)
                individual_first = individual_first + [random.randint(0,1)]
            individuos = individuos + [individual_first]
        return individuos

    def runOptimization(self):
        population = self.constructFirstPopulation()
        flags = self.getFlagOptions()
        main(population, flags) 
        
    #def main(self):
     #   self.runOptimization()


if __name__ == "__main__":
    COpt().runOptimization()
