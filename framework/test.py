from userFunctions import UserParameters
import os, subprocess
import time

class Test(UserParameters):
    """ Class to test the abstract class UserParameters 
    """
    def initial_flags(self):
        """ Implementing the method initial_flags.
            This method needs to return a list with the preferential compilation flags to be used in the evaluation
        """
        return ["-foptimize-strlen", "-fdce", "-ftree-dce", "-ftree-fre", "-ftree-coalesce-vars", "fivopts",
                "-ftree-slsr", "-fomit-frame-pointer", "-foptimize-sibling-calls", "-finline-functions",
                "-fmerge-constants", "-fmerge-all-constants", "-fthread-jumps", "-fcse-follow-jumps", 
                "-fcse-skip-blocks", "-frerun-cse-after-loop", "-fgcse", "-fgcse-lm", "-fgcse-sm", "-fcrossjumping",
                "-fif-conversion", "-fif-conversion2", "-fdelete-null-pointer-checks", "-fexpensive-optimizations",
                "-fschedule-insns", "-fschedule-insns2", "-fsched-interblock", "-fsched-spec", "-fsched-spec-load",
                "-fsched-spec-load-dangerous", "-fpeephole", "-fpeephole2", "-freorder-blocks", "-freorder-functions",
                "-fstrict-aliasing", "-falign-functions", "-falign-labels", "-falign-loops", "-falign-jumps", "-fcprop-register",
                "-fcaller-saves", "-fdefer-pop", "-ffunction-sections", "-funroll-loops", "-fdata-sections", "-ftree-pre",
                "-ftree-partial-pre", "-fpeel-loops", "-ftree-reassoc", "-ffast-math", "-ffloat-store"]

    def path_to_compile(self):
        """ Implementing the method path_to_compile.
            This method returns the path where can be found the file 
            to compile the target code (Makefile or similar)
        """ 
        pathToMake = os.getcwd() + "/cross_kalman"
        return pathToMake

    def arguments_to_compile(self):
        """ Implementing the method arguments_to_compile.
            This method returns the command to compile the target code
        """ 
        command = "make"
        return command

    def arguments_to_run_code(self):
        """ Implementing the method arguments_to_run_code.
            This method returns the command to run the executable file
        """ 
        command = "./cross_kalman -n1000"
        return command

    def evaluation_function(self, x):
        """ Implementing the method evaluation_functionn.
            This method returns the value to be optimized by the framework.
            In this method, the user needs to run the executable file and get the value to pass
            to the framework.
        """
        path_ant = os.getcwd() 
        path = os.getcwd() + "/cross_kalman"
        #path = os.getcwd()
        print path
        os.chdir(path)
        print "======= Changing directory ======="
        print os.getcwd()

        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]

        my_command = "./cross_kalman -n1000" 
        p = subprocess.Popen(my_command, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        os.chdir(path_ant)
        print "======= Changing directory ======="
        print os.getcwd()
        
        #processing the output to get the value        
        output = ''.join(out)
        #print output
        output = output.split(' ')
        d = filter(lambda c: 'throughput' in c, output)
        print "OUTPUT: ", d
        #value = output[output.index(d[1]) +4]
        #it tests if has some output
        #if haven't, put value = 0
        if len(output) > 1:
            value = output[output.index(d[1]) +4]
        else:
            value = 0.0
        print value, float(value)      
        value = float(value)


        return value 

    def path_to_clean(self):
        """ Implementing the method path_to_clea.
            This method returns the path where can be found the executable files 
            to be cleaned
        """
        path = os.getcwd() + "/cross_kalman"
        return path

    def arguments_to_clean(self):
        """ Implementing the method arguments_to_clean.
            This method returns the command to clean the target code
        """
        command = "make clean"
        return command

#x = Test()
#x.initialFlags(['a', 'b', 'c'])
#x.initialFlags(3)
#x.evaluationFunction()
# print x.pathToCompile()
# print x.argumentsToCompile()
