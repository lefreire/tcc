from abc import ABCMeta, abstractmethod
import os


class UserParameters:
    __metaclass__ = ABCMeta

    # @abc.abstractmethod
    def __init__(self):
        """Method to be implemented by the user
            Set the initial list of flags to be used in the optimization
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
            Path containing where is the file to clean the executable files
        clean_command: string
            Command indicating how to clean the executable files
            The default command is "make clean"
        min_max: value
            A value representing if the user wants to minimize ou maximize the problem
            For minimize, the value is 1 and maximize, -1
            The default is minimize
        """
        self.flags_list = ["-O1", "-O2", "-O3"]
        self.compile_path = os.getcwd()
        self.compile_command = "make"
        self.clean_path = os.getcwd()
        self.clean_command = "make clean"
        self.min_max = 1
        return

    @abstractmethod
    def arguments_to_run_code(self):
        """Method to be implemented by the user
            Method to have the way to run the executable file

        Returns
        -------
        command : string
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
