from test import Test
import os, subprocess

class runOptimizer():

    def __init__(self):
        self.testVariable =  Test()

    def runMakefile(self):
        path = self.testVariable.pathToCompile()
	os.chdir(path)
        print "======= Changing directory ======="
        print os.getcwd()

        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]
        # print my_env
        print "======= Starting make ======="
        # my_command= "make" 
        my_command = self.testVariable.argumentsToCompile()

        #call the command
        process = subprocess.Popen(my_command, env=my_env, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #get the code number 
        out = process.wait()

    
        

y = runOptimizer()
y.runMakefile()
        