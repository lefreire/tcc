from os import getcwd, chdir, environ
from subprocess import Popen, PIPE


class Pre(object):

    def __init__(self, user_class):
        self.user_class = user_class

    def __change_flags(self, individual, options):
        """ Method returns the population with the flags
            In this method, if the bool value is 1, it is switched to the correspondent flag
        """
        individual_def = ""
        for ind in xrange(0, len(individual)):
            if individual[ind] > 0.5:
                individual_def = individual_def + " " + options[ind]
        individual_def = '"' + individual_def + '"'
        return individual_def

    def compile_code(self, individual):
            """ Method to compile the target code
                This method uses methods defined by the user  
            """
            compile_path = self.user_class.compile_path
            compile_command = self.user_class.compile_command 
            flags = self.user_class.flags_list
            individual = self.__change_flags(individual, flags)
            compile_command = "CXXFLAGS="+ individual + " " + compile_command

            path = getcwd()
            chdir(compile_path)
            
            my_env = environ.copy()
            my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
            
            process = Popen(compile_command, shell=True, stdout=PIPE)
            out, err =  process.communicate()
            chdir(path)
        

