import random
import matplotlib
from PolutionNormalGame import *
from SimulationParameters import *
from Graphing import *

govExpectedReturnWithSupervision = 1
govExpectedReturnNoSupervision = 1
enterpriseExpectedReturnWithControl = 1
enterpriseExpectedReturnNoControl = 1

#probability of enterprise control = X
#probability of government supervision = Y

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

#Take inputs for variables
R = int(input("Economic Benefits of Enterprise: "))
C1 = int(input("Direct Cost of Production: "))
C2 = int(input("Pollution Control Costs for Enterprise when engaging in pollution control strategy: "))
P = int(input("Punishment costs, such as direct fines or profits lost from suspensions: "))
C3 = int(input("Government Cost of Supervision: "))
H = int(input("Repution/Public Image Return for Government: "))
Mu = float(input("Strength of Third Party Supervision; 0 < x < 1: "))
W1 = int(input("Cost of public image loss by enterprise: "))
W2 = int(input("Cost of public image loss by government: "))

'''

simulation = PolutionNormalGame(100, 80, 1, 3, 50, 60, .5, 8, 100)
print(simulation)
print(simulation.entityPayout)

parameters = SimulationParameters("entity", 100, 80, 5, 3, 50, 60, 8, 100)
Graphing(parameters)


