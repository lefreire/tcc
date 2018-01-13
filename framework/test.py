from userFunctions import UserParameters
import os, subprocess

class Test(UserParameters):
    def initialFlags(self, initialList):
        print initialList  

    def pathToCompile(self): 
        pathToMake = os.getcwd() + '/codeToTest'
        return pathToMake

    def evaluationFunction(self):
        my_command = "./nbody.gpp-3.gpp_run 50000000"
        p = subprocess.Popen(my_command, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        output = ''.join(out)
        output = output.split('\n')
        value = output[0]
        value = float(value)
        return value, 

x = Test()
x.initialFlags(['a', 'b', 'c'])
x.initialFlags(3)
print x.pathToCompile()