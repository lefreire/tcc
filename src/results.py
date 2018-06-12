from decimal import Decimal
from math import fmod
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Results(object):

    def __init__(self, user_class):
        self.tmp_values_evaluation = []
        self.min_max = 1#user_class.min_max 
        self.no_pop= 2#user_class.dict_optimization['no_pop']
        self.def_values_evaluation = []
        self.path = "./"

    def set_values_evaluation(self, value):
        self.tmp_values_evaluation.append(value)
        if fmod(len(self.tmp_values_evaluation), self.no_pop) == 0.0:
            self.set_def_values_evaluation()
            
    def set_def_values_evaluation(self):
        if self.min_max == 1:
            self.def_values_evaluation.append(min(self.tmp_values_evaluation))
        else: 
            self.def_values_evaluation.append(max(self.tmp_values_evaluation))
        self.tmp_values_evaluation = []

    def funcao_normal(self):
        print "vetor def: ", self.def_values_evaluation

    def log(self):
        print("Results:\n")
        print('{} {:^10}'.format('Generation: ', 'Value: '))
        results = list(enumerate(self.def_values_evaluation))
        for result in results:
            print('{} {:^20}'.format(result[0]+1, result[1]))

    def graphic(self):
        gen, values = zip(*list(enumerate(self.def_values_evaluation)))
        # gen, values = zip(*results)
        plt.plot(gen, values, linewidth=2.5, 
                 label  = "Island: "+ str('%.2E' % Decimal(values[-1])))
        plt.legend(bbox_to_anchor=(0.5, 0), loc=3,
                   ncol=2, mode="expand", borderaxespad=0.)
        plt.xlabel('generations')
        plt.ylabel('best evaluate')
        plt.title('Generation with: population= ' + str(self.no_pop), 
                    bbox={'facecolor': '0.8', 'pad': 5}) 
        plt.savefig("{}island_{}.png".format(self.path, str(self.no_pop)))
        # plt.savefig(str(self.no_pop)+'.png')       
