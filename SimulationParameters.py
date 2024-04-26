class SimulationParameters:

    def __init__(self, player, ecoBenefitR, prodCostC1, punishmentP, pollControlCostC2, regulationCostC3, reputationReturnH, enterpriseSocialDamageW1, governmentSocialDamageW2):
        self.player = player #which player to simulate, the government or the entity
        self.r = ecoBenefitR #revenue
        self.c1 = prodCostC1 #operation costs without pollution control
        self.p = punishmentP #cost of being discovered 
        self.c2 = pollControlCostC2 #operation costs directly tied to pollution control
        self.c3 = regulationCostC3  #government cost of pollution supervision
        self.h = reputationReturnH #government benefit of having enterprises control pollution
        self.w1 = enterpriseSocialDamageW1
        self.w2 = governmentSocialDamageW2
    
    def getPlayer(self):
        return self.player
    def getR(self):
        return self.r
    def getC1(self):
        return self.c1
    def getP(self):
        return self.p
    def getC2(self):
        return self.c2
    def getC3(self):
        return self.c3
    def getH(self):
        return self.h
    def getW2(self):
        return self.w2
    def getW1(self):
        return self.w1
    
    

