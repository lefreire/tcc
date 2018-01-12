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

    	"""
    	return

    @abc.abstractmethod
    def evaluationFunction(self):
    	"""Method to be implemented by the user
    	    Method to do the evaluation of the code to be optimized
    	"""
    	return

