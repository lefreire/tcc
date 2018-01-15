from userFunctions import UserParameters
import os, subprocess
import time

class Test(UserParameters):
	""" Class to test the abstract class UserParameters 
	"""
    def initialFlags(self, initialList):
    	""" Implementing the method initialFlags.
    	    This method needs to return a list with the preferential compilation flags to be used in the evaluation
    	"""
        print initialList  

    def pathToCompile(self):
        """ Implementing the method pathToCompile.
    	    This method returns the path where can be found the file 
    	    to compile the target code (Makefile or similar)
    	""" 
        pathToMake = os.getcwd() + "/codeToTest"
        return pathToMake

    def argumentsToCompile(self):
    	""" Implementing the method argumentsToCompile.
    	    This method returns the command to compile the target code
    	""" 
    	command = "make"
    	return command

    def argumentsToRunCode(self):
    	""" Implementing the method argumentsToRunCode.
    	    This method returns the command to run the executable file
    	""" 
    	command = "./nbody.gpp-3.gpp_run 50000000"
    	return command

    def evaluationFunction(self):
    	""" Implementing the method evaluationFunction.
    	    This method returns the value to be optimized by the framework.
    	    In this method, the user needs to run the executable file and get the value to pass
    	    to the framework.
    	""" 
        path = os.getcwd() + "/codeToTest"
        os.chdir(path)
        print "======= Changing directory ======="
        print os.getcwd()

        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]

        my_command = "./nbody.gpp-3.gpp_run 50000000" 
        #time
        t0 = time.time()
        p = subprocess.Popen(my_command, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        #time
        value = time.time() - t0
        print value
        return value, 

x = Test()
x.initialFlags(['a', 'b', 'c'])
x.initialFlags(3)
x.evaluationFunction()
# print x.pathToCompile()
# print x.argumentsToCompile()