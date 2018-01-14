# from abc import ABCMeta
import abc

class UserParameters:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def initialFlags(self, initialList):
        """Method to be implemented by the user
            Set the initial list of flags to be used in the optimization
        
        Parameters
        ----------
        initialList : list
            The list with initial flags
        """
        return

    @abc.abstractmethod
    def pathToCompile(self):
    	"""Method to be implemented by the user
    	    Method to have the path to the compiling file

        Returns
        -------
        path : string
            Path indicating where can be find the file to compile the target code.
    	"""
    	return

    @abc.abstractmethod
    def argumentsToCompile(self):
        """Method to be implemented by the user
            Method to have the way to run the Makefile or similar

        Returns
        -------
        command : string
            Command indicating how to run the file to compile the code.
        """
        return 

    @abc.abstractmethod
    def argumentsToRunCode(self):
        """Method to be implemented by the user
            Method to have the way to run the executable file

        Returns
        -------
        command : string
            Command indicating how to run the executable file.
        """
        return

    @abc.abstractmethod
    def evaluationFunction(self):
    	"""Method to be implemented by the user
    	    Method to do the evaluation of the code to be optimized

        Returns
        -------
        value : float
            This method returns the value to be optimized.
    	"""
    	return

