# from abc import ABCMeta
import abc

class UserParameters:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def initial_flags(self):
        """Method to be implemented by the user
            Set the initial list of flags to be used in the optimization
        
        Parameters
        ----------
        initialList : list
            The list with initial flags
        """
        return

    @abc.abstractmethod
    def path_to_compile(self):
        """Method to be implemented by the user
            Method to have the path to the compiling file

        Returns
        -------
        path : string
            Path indicating where can be find the file to compile the target code.
        """
        return

    @abc.abstractmethod
    def arguments_to_compile(self):
        """Method to be implemented by the user
            Method to have the way to run the Makefile or similar

        Returns
        -------
        command : string
            Command indicating how to run the file to compile the code.
        """
        return 

    @abc.abstractmethod
    def arguments_to_run_code(self):
        """Method to be implemented by the user
            Method to have the way to run the executable file

        Returns
        -------
        command : string
            Command indicating how to run the executable file.
        """
        return

    @abc.abstractmethod
    def evaluation_function(self, x):
        """Method to be implemented by the user
            Method to do the evaluation of the code to be optimized

        Returns
        -------
        value : float
            This method returns the value to be optimized.
        """
        return

    @abc.abstractmethod
    def path_to_clean(self):
        """Method to be implemented by the user
            Method to have the way to run the Makefile or similar to clean the executable files

        Returns
        -------
        path : string
            Command indicating how to clean the executable files.
        """
        return 

    @abc.abstractmethod
    def arguments_to_clean(self):
        """Method to be implemented by the user
           Method to have the way to run the clean the executable files

        Returns
        -------
        command : string 
            Command indicating how to clean the executable files.
        """
        return 
