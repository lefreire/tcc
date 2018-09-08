from os import getcwd, chdir, environ
from subprocess import Popen, PIPE


class CompClean(object):
    """ Class to compile the code and clean the executable files
    """

    def __init__(self, user_class):
        self.user_class = user_class

    def __change_flags(self, individual, options, no_individuals):
        """ Method returns the population with the flags
        In this method, if the bool value is 1, 
        it is switched to the correspondent flag

        Returns
        -------
        individual_def : list
            List containing the chosen flags to be 
            used in the compilation.
        """
        individual_def = ""
        for ind in range(0, len(individual)):
            if individual[ind] > 0.5:
                individual_def = individual_def + " " + options[ind]
        individual_def = individual_def + " " + self.user_class.static_flags
        individual_def = '"' + individual_def + '"'
        return individual_def

    def compile_code(self, individual):
        """ Method to compile the target code
            This method uses methods defined by the user  
        """
        compile_path = self.user_class.compile_path
        compile_command = self.user_class.compile_command
        flags = self.user_class.flags_list
        no_individuals = self.user_class.dict_optimization["individual_size"]
        individual = self.__change_flags(individual, flags, no_individuals)
        compile_command = "{}={} {}".format(
            self.user_class.macro, individual, compile_command)

        path = getcwd()
        chdir(compile_path)


        my_env = environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:{}".format(my_env["PATH"])

        process = Popen(compile_command, shell=True, stdout=PIPE)
        out, err = process.communicate()
        chdir(path)

    def clean_code(self):
        """ Method to clean the target code
            This method uses methods defined by the user
            It cleans all the executable files
        """
        path = getcwd()
        clean_path = self.user_class.clean_path
        clean_command = self.user_class.clean_command

        chdir(clean_path)

        my_env = environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:{}".format(my_env["PATH"])

        process = Popen(clean_command, shell=True, stdout=PIPE)
        out, err = process.communicate()
        chdir(path)
