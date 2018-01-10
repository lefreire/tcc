# import abc
# from base import UserOptimizer
# import userFunctions
from userFunctions import UserOptimizer

class Test(UserOptimizer):
    def initialFlags(self, initialList):
        print initialList    

x = Test()
x.initialFlags(['a', 'b', 'c'])
x.initialFlags(3)