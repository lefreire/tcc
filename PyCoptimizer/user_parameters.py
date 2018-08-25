from abc import ABCMeta, abstractmethod
from os import getcwd


class UserParameters(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        """Method to be implemented by the user
            Set the initial list of flags to be used in the 
            optimization
            Set the path to compile
            Set if the user wants to minize or maximize the problem
        Parameters
        ----------
        flags_list: list
            The list with initial flags
            The default list is composed with flags for gcc compiler
        compile_path: string
            Path containing where is the file to compile
        compile_command: string
            Command indicating how to compile the code
            The default command is "make"
        clean_path: string
            Path containing where is the file to clean the executable 
            files
        clean_command: string
            Command indicating how to clean the executable files
            The default command is "make clean"
        min_max: value
            A value representing if the user wants to minimize or 
            maximize the problem
            For minimize, the value is 1 and maximize, -1
            The default is minimize
        macro: string
            String to indicate to the compiler the flags to be used.
        method_optimization: string
            String containing the name of the method to do 
            the optimization.
            The string can be: island.
        dict_optimization: dictionary
            This dictionary needs to have all information for the 
            optimization method. 
            For the island method, you must give these informations:
                -no_generations: number of generations
                -no_pop: population size
                -individual_size: individual size; this size must be 
                equal than the number of flags in the 
                flags_list
                -crossover_rate: crossover rate; must be between 0 
                and 1
                -mutation_rate: mutation rate; must be between 0 and 1
        static_flags: string
            String containing flags that will be used in every compilation.    
        """
        self.flags_list = ["-O1", "-O2", "-O3"]
        self.compile_path = getcwd()
        self.compile_command = "make"
        self.clean_path = getcwd()
        self.clean_command = "make clean"
        self.min_max = 1
        self.macro = "CXXFLAGS"
        self.method_optimization = "island"
        self.dict_optimization = {"no_generations": 3,
                                  "no_pop": 2,
                                  "individual_size": 3,
                                  "crossover_rate": 0.3,
                                  "mutation_rate": 0.1}
        self.static_flags = ""
        return

    @abstractmethod
    def pre(self):
        """Method to be implemented by the user
           This method will be executed before every compilation and evaluation.
        """
        return

    @abstractmethod
    def arguments_to_run_code(self):
        """Method to be implemented by the user
        Method to have the way to run the executable file 

        Returns
        -------
        command: string
        Command indicating how to run the executable file.

        """
        return

    @abstractmethod
    def evaluation_function(self, x):
        """Method to be implemented by the user
            Method to do the evaluation of the code to be optimized

        Returns
        -------
        value : float
            This method returns the value to be optimized.
        """
        return

    @abstractmethod
    def pos(self):
        """Method to be implemented by the user
           This method will be executed after cleaning the executable files.
        """
        return
