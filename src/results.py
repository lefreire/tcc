from decimal import Decimal
from math import fmod
import matplotlib
matplotlib.use('Agg')
import matplotlib.image as mpimg
import matplotlib.pyplot as plt


class Results(object):

    def __init__(self, user_class):
        self.tmp_values_evaluation = []
        self.min_max = user_class.min_max 
        self.no_pop= user_class.dict_optimization['no_pop']
        self.def_values_evaluation = []

    def set_values_evaluation(self, value):
        self.tmp_values_evaluation.append(value)
        if fmod(len(self.tmp_values_evaluation), self.no_pop) == 0.0:
            self.set_def_values_evaluation()
        print "valores: ", self.def_values_evaluation

    def set_def_values_evaluation(self):
        if self.min_max == 1:
            self.def_values_evaluation.append(min(self.tmp_values_evaluation))
        else: 
            self.def_values_evaluation.append(max(self.tmp_values_evaluation))
        self.tmp_values_evaluation = []

    def get_graphic(self):
        print self.min_max
        print "valor final: ", self.def_values_evaluation
        plt.plot(len(self.def_values_evaluation), self.def_values_evaluation, 
                linewidth=2.5) 
        #         label  = "Pygmo: "+ str('%.2E' % Decimal(-logs[-1][2])))
        # plt.legend(bbox_to_anchor=(0.5, 0), loc=3,
        #        ncol=2, mode="expand", borderaxespad=0.)
        plt.xlabel('generations')
        plt.ylabel('best evaluate')
        plt.title('Generation with: population= ' + str(self.no_pop), 
                    bbox={'facecolor': '0.8', 'pad': 5}) 
        plt.savefig(str(self.no_pop)+'.png')       