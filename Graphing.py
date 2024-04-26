import matplotlib.pyplot as plt
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

        plt.title(self.player + " Average Payout")
        plt.ylabel('Average Payout')
        plt.xlabel('Probability of Third Party Supervision')
        plt.plot(self.payoutData)
        plt.show()

    def generatePayoutData(self):
        self.payoutData = []
        for i in range(100):
            plotPoint = 0
            for j in range(10):

                normalGame = PolutionNormalGame(self.r, self.c1, self.p, self.c2, self.c3, self.h, i*.01, self.w1, self.w2)

                if self.player == "government":
                    plotPoint = plotPoint + (normalGame.getGovernmentPayout())
                if self.player == "entity":
                    plotPoint = plotPoint + (normalGame.getEntityPayout())

            plotPoint = plotPoint / 10
            self.payoutData.append(plotPoint)
                
            
    
