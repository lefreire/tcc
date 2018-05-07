from src.userFunctions import UserParameters
import os
import subprocess
import time

class Test(UserParameters):
    """ Class to test the abstract class UserParameters 
    """

    def __init__(self):
        super(Test, self).__init__()
        self.compile_path = os.getcwd() + "/codeToTest"
        self.clean_path = os.getcwd() + "/codeToTest"

    def arguments_to_run_code(self):
        """ Implementing the method arguments_to_run_code.
            This method returns the command to run the executable file
        """ 
        return"./nbody.gpp-3.gpp_run 50000000"

    def evaluation_function(self):
        """ Implementing the method evaluation_functionn.
            This method returns the value to be optimized by the framework.
            In this method, the user needs to run the executable file and get the value to pass
            to the framework.
        """
        def_path = os.getcwd() 
        os.chdir(self.compile_path)

        my_env = os.environ.copy()
        my_env["PATH"] = "/usr/sbin:/sbin:" + my_env["PATH"]

        my_command = self.arguments_to_run_code()
        #counting time 
        t0 = time.time()
        p = subprocess.Popen(my_command, shell=True, stdout=subprocess.PIPE)
        out, err =  p.communicate()
        #finalizing
        value = time.time() - t0

        os.chdir(def_path)
    
        return value 


x = Test()
print x.macro
# print x.evaluation_function()
