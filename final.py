import random
import matplotlib
from PolutionNormalGame import *
from SimulationParameters import *
from Graphing import *

'''
R: Economic Benefits of enterprise
C1: Direct cost of production
C2: Pollution Control Costs, created when enterprise engages in pollution control strategy
P: Punishment; costs such as fines or business suspensions
C3: Government cost of supervision
H: Reputation/Public Image return for government
Mu: Probability of supervision observing discharge behaviors of enterprises, 0<Mu<1; expresses the 'strength' of third party supervision
W1: Cost of public image loss by enterprise
W2: Cost of public image loss by government

When Mu = 0, there is no supervision and pollution discharge is not observed, resulting in return of R-C1+H for enterprise and government
When Mu = 1, return of enterprise is R-C1-W1, and return of government is -W2

ASSUMPTION: Government regulation, when C3 is implemented, is assumed to discover pollution discharge behavior before third party due to constraints on third
party observation

ASSUMPTION: When P < C2, the government punishment mechanism fails and the enterprise will not engage in pollution control.  So we must assume that P > C2 in
in order to have impact.
'''

parameters = SimulationParameters("entity", 100, 80, 5, 3, 50, 60, 8, 100)
Graphing(parameters).lineColors

simulation = PolutionNormalGame(parameters.getR(), parameters.getC1(), parameters.getP(), parameters.getC2(), parameters.getC3(), parameters.getH(), .5, parameters.getW1(), parameters.getW2())
print(simulation)

