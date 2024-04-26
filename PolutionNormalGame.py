import random

class PolutionNormalGame:
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

        #creates a representation of the normal form game using a multilayered python dictionary.
        self.normalFormGraph = self.createNormalGraph()       
        self.calculatePayout("government")
        self.calculatePayout("entity")
    
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
    
    def getGovernmentPayout(self):
        return self.governmentPayout
    
    def getEntityPayout(self):
        return self.entityPayout

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
    
    def findMixedStrategy(self, player):
        quadrant1 = self.normalFormGraph.get(player).get("supervisionPollutionControl")
        quadrant2 = self.normalFormGraph.get(player).get("noSupervisionPollutionControl")
        quadrant3 = self.normalFormGraph.get(player).get("supervisionNoPollutionControl")
        quadrant4 = self.normalFormGraph.get(player).get("noSupervisionNoPollutionControl")


    def findStrategy(self, player):        
        quadrant1 = self.normalFormGraph.get(player).get("supervisionPollutionControl")
        quadrant2 = self.normalFormGraph.get(player).get("noSupervisionPollutionControl")
        quadrant3 = self.normalFormGraph.get(player).get("supervisionNoPollutionControl")
        quadrant4 = self.normalFormGraph.get(player).get("noSupervisionNoPollutionControl")

        opponentQuadrant1 = self.normalFormGraph.get("government").get("supervisionPollutionControl")

        if player == "entity":
            opponentQuadrant1 = self.normalFormGraph.get("government").get("supervisionPollutionControl")
            opponentQuadrant2 = self.normalFormGraph.get("government").get("noSupervisionPollutionControl")
            opponentQuadrant3 = self.normalFormGraph.get("government").get("supervisionNoPollutionControl")
            opponentQuadrant4 = self.normalFormGraph.get("government").get("noSupervisionNoPollutionControl")

            #if one strategy always results in a higher payoff no matter what the other player chooses, choose that strategy
            if quadrant1 > quadrant3 and quadrant2 > quadrant4:
                self.entityStrategy = "pollutionControl"
            elif quadrant3 > quadrant1 and quadrant4 > quadrant2:
                self.entityStrategy = "noPollutionControl"

            #if the other player has a dominant strategy, assume they will go for that strategy and choose the strategy that results in a higher payoff for you
            elif opponentQuadrant1 > opponentQuadrant2 and opponentQuadrant3 > opponentQuadrant4:
                if quadrant1 > quadrant3:
                    self.entityStrategy = "pollutionControl"
                elif quadrant3 > quadrant1:
                    self.entityStrategy = "noPollutionControl"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        self.entityStrategy = "pollutionControl"
                    else:
                        self.entityStrategy = "noPollutionControl"
            elif opponentQuadrant2 > opponentQuadrant1 and opponentQuadrant4 > opponentQuadrant3:
                if quadrant2 > quadrant4:
                    self.entityStrategy = "pollutionControl"
                elif quadrant4 > quadrant2:
                    self.entityStrategy = "noPollutionControl"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        self.entityStrategy = "pollutionControl"
                    else:
                        self.entityStrategy = "noPollutionControl"
            else:
                randomStrat = random.randint(0,1)
                if randomStrat == 0:
                    self.entityStrategy = "pollutionControl"
                else:
                    self.entityStrategy = "noPollutionControl"

        if player == "government":
            opponentQuadrant1 = self.normalFormGraph.get("entity").get("supervisionPollutionControl")
            opponentQuadrant2 = self.normalFormGraph.get("entity").get("noSupervisionPollutionControl")
            opponentQuadrant3 = self.normalFormGraph.get("entity").get("supervisionNoPollutionControl")
            opponentQuadrant4 = self.normalFormGraph.get("entity").get("noSupervisionNoPollutionControl")

            #if one strategy always results in a higher payoff no matter what the other player chooses, choose that strategy
            if quadrant1 > quadrant2 and quadrant3 > quadrant4:
                self.governmentStrategy = "supervision"
            elif quadrant2 > quadrant1 and quadrant4 > quadrant3:
                self.governmentStrategy = "noSupervision"

            #if the other player has a dominant strategy, assume they will go for that strategy and choose the strategy that results in a higher payoff for you
            elif opponentQuadrant1 > opponentQuadrant3 and opponentQuadrant2 > opponentQuadrant4:
                if quadrant1 > quadrant2:
                    self.governmentStrategy = "supervision"
                elif quadrant2 > quadrant1:
                    self.governmentStrategy = "noSupervision"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        self.governmentStrategy = "supervision"
                    else:
                        self.governmentStrategy = "noSupervision"                        
            elif opponentQuadrant3 > opponentQuadrant1 and opponentQuadrant4 > opponentQuadrant2:
                if quadrant3 > quadrant4:
                    self.governmentStrategy = "supervision"
                elif quadrant4 > quadrant3:
                    self.governmentStrategy = "noSupervision"
                #if both payouts are the same, pick one at random
                else:
                    randomStrat = random.randint(0,1)
                    if randomStrat == 0:
                        self.governmentStrategy = "supervision"
                    else:
                        self.governmentStrategy = "noSupervision"
            else:
                randomStrat = random.randint(0,1)
                if randomStrat == 0:
                    self.governmentStrategy = "supervision"
                else:
                    self.governmentStrategy = "noSupervision"
    
    def calculatePayout(self, player):
        self.findStrategy("government")
        self.findStrategy("entity")
        if player == "entity":
            self.entityPayout = self.normalFormGraph.get(player).get(self.governmentStrategy + self.entityStrategy[0].upper() + self.entityStrategy[1:])
        elif player == "government":
            self.governmentPayout = self.normalFormGraph.get(player).get(self.governmentStrategy + self.entityStrategy[0].upper() + self.entityStrategy[1:])

    '''
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