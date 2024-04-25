import random

govExpectedReturnWithSupervision = 1
govExpectedReturnNoSupervision = 1
enterpriseExpectedReturnWithControl = 1
enterpriseExpectedReturnNoControl = 1

#probability of enterprise control = X
#probability of government supervision = Y

class PolutionSimulation:
    def __init__(self, ecoBenefitR, prodCostC1, punishmentP, pollControlCostC2, regulationCostC3, reputationReturnH, thirdPartySupervisionMu, enterpriseSocialDamageW1, governmentSocialDamageW2):
        self.r = ecoBenefitR #revenue
        self.c1 = prodCostC1 #operation costs without pollution control
        self.p = punishmentP #cost of being discovered 
        self.c2 = pollControlCostC2 #operation costs directly tied to pollution control
        self.c3 = regulationCostC3  #government cost of pollution supervision
        self.h = reputationReturnH #government benefit of having enterprises control pollution
        self.mu = thirdPartySupervisionMu 
        self.w1 = enterpriseSocialDamageW1
        self.w2 = governmentSocialDamageW2
        self.normalFormGraph = self.createNormalGraph()
    
    def __str__(self):
        string = "\n"
        whitespace = "                    "
        string = string + whitespace + "Supervision".center(20) + "No Supervision".center(20) + "\n"
        string = string + "-" * 60 + "\n"
        string = string + "Pollution control".center(20) + ("("+str(self.normalFormGraph.get("entity").get("supervisionPollutionControl")) + ", " + str(self.normalFormGraph.get("government").get("supervisionPollutionControl")) + ")").center(20)
        string = string + ("(" + str(self.normalFormGraph.get("entity").get("noSupervisionPollutionControl")) + ", " + str(self.normalFormGraph.get("government").get("noSupervisionPollutionControl")) + ")").center(20) + "\n"
        string = string + "No Pollution control".center(20) + ("(" + str(self.normalFormGraph.get("entity").get("supervisionNoPollutionControl")) + ", " + str(self.normalFormGraph.get("government").get("supervisionNoPollutionControl")) + ")").center(20)
        string = string + ("(" + str(self.normalFormGraph.get("entity").get("noSupervisionNoPollutionControl")) + ", " + str(self.normalFormGraph.get("government").get("noSupervisionNoPollutionControl")) + ")").center(20)
        return string

    def createNormalGraph(self):
        supervisionPollutionControl = (self.r-self.c1-self.c2, self.h-self.c3)
        noSupervisionPollutionControl = (self.r-self.c1-self.c2, self.h)
        supervisionNoPollutionControl = (self.r-self.c1-self.p, self.h-self.c3)
        noSupervisionNoPollutionControl = (self.r-self.c1-(self.mu*self.w1), (1-self.mu)*self.h-(self.mu*self.w2))

        governmentDictionary = {
            "supervisionPollutionControl" : supervisionPollutionControl[1],
            "noSupervisionPollutionControl" : noSupervisionPollutionControl[1],
            "supervisionNoPollutionControl" : supervisionNoPollutionControl[1],
            "noSupervisionNoPollutionControl" :noSupervisionNoPollutionControl[1]
        }

        entityDictionary = {
            "supervisionPollutionControl" : supervisionPollutionControl[0],
            "noSupervisionPollutionControl" : noSupervisionPollutionControl[0],
            "supervisionNoPollutionControl" : supervisionNoPollutionControl[0],
            "noSupervisionNoPollutionControl" :noSupervisionNoPollutionControl[0]
        }

        normalFormGraph = {
            "government" : governmentDictionary,
            "entity" : entityDictionary
        }
        
        return normalFormGraph
    
    def findStrategy(self, player):        
        quadrant1 = self.normalFormGraph.get(player).get("supervisionPollutionControl")
        quadrant2 = self.normalFormGraph.get(player).get("noSupervisionPollutionControl")
        quadrant3 = self.normalFormGraph.get(player).get("supervisionNoPollutionControl")
        quadrant4 = self.normalFormGraph.get(player).get("noSupervisionNoPollutionControl")

        if player == "entity":
            #if one strategy always results in a higher payoff no matter what the other player chooses, choose that strategy
            if quadrant1 > quadrant3 and quadrant2 > quadrant4:
                strategy = "pollutionControl"
            elif quadrant3 > quadrant1 and quadrant4 > quadrant2:
                strategy = "noPollutionControl"

            #if the other player has a dominant strategy, assume they will go for that strategy and choose the strategy that results in a higher payoff for you
            elif quadrant1 > quadrant2 and quadrant3 > quadrant4:
                if quadrant1 > quadrant3:
                    strategy = "pollutionControl"
                elif quadrant3 > quadrant1:
                    strategy = "noPollutionControl"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        strategy = "supervision"
                    else:
                        strategy = "noSupervision"
            elif quadrant2 > quadrant1 and quadrant4 > quadrant3:
                if quadrant2 > quadrant4:
                    strategy = "pollutionControl"
                elif quadrant4 > quadrant2:
                    strategy = "noPollutionControl"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        strategy = "supervision"
                    else:
                        strategy = "noSupervision"
            
        if player == "government":
            #if one strategy always results in a higher payoff no matter what the other player chooses, choose that strategy
            if quadrant1 > quadrant2 and quadrant3 > quadrant4:
                strategy = "supervision"
            elif quadrant2 > quadrant1 and quadrant4 > quadrant3:
                strategy = "noSupervision"

            #if the other player has a dominant strategy, assume they will go for that strategy and choose the strategy that results in a higher payoff for you
            elif quadrant1 > quadrant3 and quadrant2 > quadrant4:
                if quadrant1 > quadrant2:
                    strategy = "supervision"
                elif quadrant2 > quadrant1:
                    strategy = "noSupervision"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        strategy = "supervision"
                    else:
                        strategy = "noSupervision"                        
            elif quadrant3 > quadrant1 and quadrant4 > quadrant2:
                if quadrant3 > quadrant4:
                    strategy = "supervision"
                elif quadrant4 > quadrant3:
                    strategy = "noSupervision"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        strategy = "supervision"
                    else:
                        strategy = "noSupervision"
                                
    #returns true if government chooses to supervise and false if government chooses not to supervise
    def chooseGovStrat(probabilityOfControl):
        if (govExpectedReturnWithSupervision > govExpectedReturnNoSupervision):
            return True
        else:
            return False

    #returns true if enterprise chooses to control pollution emissions and false if enterprise chooses not to control
    def chooseEnterpriseStrat(probabilityOfSupervision):
        if (enterpriseExpectedReturnWithControl > enterpriseExpectedReturnNoControl):
            return True
        else:
            return False

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
simulation = PolutionSimulation(100, 80, 5, 3, 50, 60, .5, 8, 100)
print(simulation)
