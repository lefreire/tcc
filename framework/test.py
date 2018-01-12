from userFunctions import UserParameters

class Test(UserParameters):
    def initialFlags(self, initialList):
        print initialList    

x = Test()
x.initialFlags(['a', 'b', 'c'])
x.initialFlags(3)