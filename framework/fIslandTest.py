import random

#for pygmo evolution
#from my_problem import *



#deap code
#arguments for genetic function
args = 5*[0]
args[0] = 50 #number of generations
args[1] = 10 # size of population
args[2] = 6 #size of individual
args[3] = 0.3 #crossover rate
args[4] = 0.1 #mutation rate
individuos = []
individuos_def = []
options = ['-O', '-O1', '-O2', '-O3', '-O0', '-Os'];


for ind in xrange(0, args[1]):
    individual_first = []
    for individual in xrange(0, args[2]):
        #individual_bool = random.randint(0,1)
        individual_first = individual_first + [random.randint(0,1)]
    individuos = individuos + [individual_first]

for ind in xrange(0, args[1]):
    individual_first = []
    for individual in xrange(0, args[2]):
        if individuos[ind][individual]:
            individual_first = individual_first + [options[individual]]
    individuos_def = individuos_def + [individual_first]

print "INDIVIDUOS: ", individuos_def


#for pygmo evolution
#from my_problem import *
#main(individuos)

