from decimal import Decimal
from math import fmod
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Results(object):

    def __init__(self, user_class, result_type, path='./'):
        """ Constructor

        Parameters
        ----------
        user_class: class defined by the user
        result_type: resolve if the result will be printed in the screen or
                    will be in the graphic
        path: path where to save the results 
        """
        self.no_pop = user_class.dict_optimization['no_pop']
        self.path = path
        self.result_type = result_type

    def log(self, list_generations, list_values):
        """ Method to print in the screen the main results
        """
        print("Results:\n")
        print('{} {:^10}'.format('Generation: ', 'Value: '))
        for res in range(len(list_generations)):
            print('{} {:^20}'.format(list_generations[res], list_values[res]))

    def graphic(self, list_generations, list_values):
        """ Method to draw in a graphic the main results
        """
        plt.plot(list_generations, list_values, linewidth=2.5,
                 label="Island: " + str('%.2E' % Decimal(list_values[-1])))
        plt.legend(bbox_to_anchor=(0.5, 0), loc=3,
                   ncol=2, mode="expand", borderaxespad=0.)
        plt.xlabel('generations')
        plt.ylabel('best evaluate')
        plt.title('Generation with: population= ' + str(self.no_pop),
                  bbox={'facecolor': '0.8', 'pad': 5})
        plt.savefig("{}island_{}.png".format(self.path, str(self.no_pop)))

    def get_results(self, list_generations, list_values):
        """ Method to choose how the user wants to see their results
        """
        if self.result_type == 'log':
            self.log(list_generations, list_values)
        else:
            self.graphic(list_generations, list_values)
