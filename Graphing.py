import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.patches as mpatches
import numpy as np
from PolutionNormalGame import *

class Graphing:

    def __init__(self, simulationParameters):
        self.player = simulationParameters.getPlayer()
        self.r = simulationParameters.getR()
        self.c1 = simulationParameters.getC1()
        self.p = simulationParameters.getP()
        self.c2 = simulationParameters.getC2()
        self.c3 = simulationParameters.getC3()
        self.h = simulationParameters.getH()
        self.w1 = simulationParameters.getW1()
        self.w2 = simulationParameters.getW2()

        self.generatePayoutData()
        self.colorLinesBasedOnStrategy()
        

    def generatePayoutData(self):
        self.payoutData = []
        self.lineColors = []

        for i in range(100):
            plotPoint = 0
            for j in range(10):
                normalGame = PolutionNormalGame(self.r, self.c1, self.p, self.c2, self.c3, self.h, i*.01, self.w1, self.w2)
                positiveStratCount = 0
                negativeStratCount = 0

                if self.player == "government":
                    plotPoint = plotPoint + (normalGame.getGovernmentPayout())
                    if normalGame.getGovernmentStrategy() == "supervision":
                        positiveStratCount = positiveStratCount +  1
                    elif normalGame.getGovernmentStrategy() == "noSupervision":
                        negativeStratCount = negativeStratCount + 1
                if self.player == "entity":
                    plotPoint = plotPoint + (normalGame.getEntityPayout())
                    if normalGame.getEntityStrategy() == "pollutionControl":
                        positiveStratCount = positiveStratCount + 1
                    elif normalGame.getEntityStrategy() == "noPollutionControl":
                        negativeStratCount = negativeStratCount + 1

            if positiveStratCount > negativeStratCount:
                self.lineColors.append('blue')
            elif negativeStratCount > positiveStratCount:
                self.lineColors.append('red')
            
            plotPoint = plotPoint / 10

            self.payoutData.append(plotPoint)

    def colorLinesBasedOnStrategy(self):
        y = np.array(self.payoutData)
        x = np.arange(len(y))

        segments_x = np.r_[x[0], x[1:-1].repeat(2), x[-1]].reshape(-1, 2)
        segments_y = np.r_[y[0], y[1:-1].repeat(2), y[-1]].reshape(-1, 2)

        segments = [list(zip(x_, y_)) for x_, y_ in list(zip(segments_x, segments_y))]

        plt.figure()
        ax = plt.axes()

        ax.add_collection(LineCollection(segments, colors=self.lineColors))

        ax.set_xlim(0,100)

        buffer = (y.max() - y.min()) / 10 * 3

        ax.set_ylim(y.min() - buffer, y.max() + buffer)

        if (self.player == "government"):
            redLabel = "No Supervision"
            blueLabel = "Supervision"
        elif (self.player == "entity"):
            redLabel = "No Polution Control"
            blueLabel = "Polution Control"
        
        red_patch = mpatches.Patch(color='red', label=redLabel)
        blue_patch = mpatches.Patch(color='blue', label = blueLabel)

        ax.legend(handles=[red_patch, blue_patch])

        plt.title(self.player.capitalize() + " Average Payout")
        plt.ylabel('Average Payout')
        plt.xlabel('Probability of Third Party Supervision')
        plt.show()


                
            
    
