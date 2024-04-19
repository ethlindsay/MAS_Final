govExpectedReturnWithSupervision = 1
govExpectedReturnNoSupervision = 1
enterpriseExpectedReturnWithControl = 1
enterpriseExpectedReturnNoControl = 1

class PolutionSimulation:
    def __init__(self, ecoBenefitR, prodCostC1, punishmentP, pollControlCostC2, regulationCostC3, reputationReturnH, thirdPartySupervisionMew, enterpriseSocialDamageW1, governmentSocialDamageW2):
        self.r = ecoBenefitR
        self.c1 = prodCostC1
        self.p = punishmentP
        self.c2 = pollControlCostC2
        self.c3 = regulationCostC3
        self.h = reputationReturnH
        self.mew = thirdPartySupervisionMew
        self.w1 = enterpriseSocialDamageW1
        self.w2 = governmentSocialDamageW2

    #TODO
    def simulateUsingGrimTrigger():
        return
    
    #TODO 
    def simulateUsingCooperation():
        return

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
