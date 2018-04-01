import pygmo as pg

#inspecting the problem
prob = pg.problem(pg.rosenbrock(dim = 5))
print prob
#number of fitness evaluations
print prob.get_fevals() == 0


print prob.fitness([1,2,3,4,5])

print prob.get_fevals() == 1
