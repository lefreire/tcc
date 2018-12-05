from pygmo import problem, population, algorithm, sga
from PyCoptimizer.framework.comp_clean import CompClean
from PyCoptimizer.results import Results


class Island(object):
    """ Class to run the optimizer using the island method 
        The island method is provided by the pygmo module
    """

    def __init__(self, user_class, population):
        """ Constructor
        Parameters
        ----------
        user_class: class
            Class provided by the user
        dim: value
            It represents the number of flags to be used, 
            the dimension of the problem
        compClean: class
            Class to compile the code and clean the executable files
        no_pop: value
            Value containing the population size
        no_generations: value
            Value containing the number of generations
        no_individuals: value
            Value containing the individual size (number of genes)
        crossover_rate: value
            Crossover rate to be used in the genetic algorithm
        mutation_rate: value
            Mutation rate to be used in the genetic algorithm
        population: list
            List containing the inicial flags to be used
        prob: class
            Problem defined by pygmo
        pop: class
            Population defined by pygmo
        """
        self.user_class = user_class
        self.dim = len(self.user_class.flags_list)
        self.compClean = CompClean(self.user_class)
        self.no_pop = 0
        self.no_generations = 0
        self.no_individuals = 0
        self.crossover_rate = 0
        self.mutation_rate = 0
        self.population = population
        self.prob = None
        self.pop = None

    def defining_values(self):
        """ Method to set the class parameters defined 
            in the constructor
        """
        self.no_pop = self.user_class.dict_optimization["no_pop"]
        self.no_generations = self.user_class.\
            dict_optimization["no_generations"]
        self.no_individuals = self.user_class.\
            dict_optimization["individual_size"]
        self.crossover_rate = self.user_class.\
            dict_optimization["crossover_rate"]
        self.mutation_rate = self.user_class.\
            dict_optimization["mutation_rate"]
        self.prob = problem(self)
        self.pop = self.create_population(self.prob, self.population)

    def fitness(self, x):
        """ Method to calculate the fitness value
        This method uses methods defined by the user
        The method name and the return is required for the 
        pygmo structure to work the island method

        Returns
        -------
        y : float
            This method returns the fitness value.
        """
        self.user_class.pre()
        self.compClean.compile_code(x)
        y = self.user_class.evaluation_function()
        self.compClean.clean_code()
        self.user_class.pos()
        return [self.user_class.min_max*y]

    def get_bounds(self):
        """ Method returns the bound values
        The method name and the return is required for the 
        pygmo structure to work the island method
        Returns
        -------
        bounds : tuple
            This method returns the bounds of the problem.
        """
        return ([0] * self.dim, [1] * self.dim)

    def create_population(self, prob, population_list):
        """ Method to set the population using push_back method

        Returns
        -------
        pop : Population instance
            This method returns an instance of Population class.
        """
        pop = population(prob)
        for i in range(0, self.no_pop):
            pop.push_back(x=population_list[i])
        return pop

    def island_method(self, population, flag_option, user_class):
        """ Method to run the optimizer
        In this optimizer, it will be used the genetic algorithm, 
        provided by pygmo module
        This method will return a tuple with the generation 
        and their correspondent best evaluation

        Returns
        -------
        log : tuple
            This method returns a tuple containg 
            the generations and their corresponding est evaluations.
        """
        self.defining_values()
        algo = algorithm(sga(gen=self.no_generations,
                             cr=self.crossover_rate,
                             m=self.mutation_rate,
                             selection="tournament"))


        algo.set_verbosity(2)
        self.pop = algo.evolve(self.pop)
        logs = algo.extract(sga).get_log()
        return ([gen[0] for gen in logs], [val[2] for val in logs],
                self.pop.champion_x)


def main(user_class, population, flag_option, results):
    """ Main method to call the island method
    """
    island = Island(user_class, population)
    generations, values, best_ind = island.island_method(
        population, flag_option, user_class)
    results.get_results(generations, values, best_ind)


if __name__ == "__main__":
    main()
