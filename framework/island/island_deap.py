import sys
print sys.path.insert(0, './opt-compilation/')

#for deap evolution
from geneticFlags import *
from individualFlags import *
from populationFlags import *
from testsFlags import *

#for pygmo evolution
#from my_problem import *

#for create directories
#import os


#deap code
#arguments for genetic function
args = 5*[0]
args[0] = 50 #number of generations
args[1] = 150 # size of population
args[2] = 51 #size of individual
args[3] = 0.3 #crossover rate
args[4] = 0.1 #mutation rate
individuos = []


#starting with the same population
pop = PopulationFlags(args[1])
genetic = GeneticFlags()
#input
lista = range(100000)
#construct the first population
pop.constructPop(lista, args[2], args[3], args[4])

#taking the first population
for ind in pop.population:
    individual_first = []
    for individual in ind.individual:
        individual_first = individual_first + [individual[0]]
    individuos = individuos + [individual_first]


print "INDIVIDUOS: ", individuos


#make TestsFlags object
tests = TestsFlags(genetic, args[0], args[2], args[1], args[4], args[3])
listGenerations = [args[0]]
tests.changePopSize(pop, listGenerations)


#for pygmo evolution
from my_problem import *
main(individuos)
