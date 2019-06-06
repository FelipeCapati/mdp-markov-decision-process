from mdp.GridRules import GridRules
from enum import Enum
import numpy as np


class Policy(GridRules):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "POLICY"
        self.data = np.ones([x, y]) * 15  # Initialize with random policy
        self.stable = False

    class PolicyEnum(Enum):
        U = 1
        L = 2
        R = 3
        D = 4
        UL = 5
        UR = 6
        UD = 7
        LR = 8
        LD = 9
        RD = 10
        ULR = 11
        ULD = 12
        URD = 13
        LRD = 14
        ULRD = 15

    def policyUpdateByState(self, dataState):
        for s in self.arrayState:
            self.stateNow = s
            pos = self.getArrayCartesianStateByStateNow()
            y = pos[0] - 1
            x = pos[1] - 1

            futureStateUP = self.getArrayCartesianStateByStaticState(self.getFutureStateByAction(self.Action.UP))
            futureStateLEFT = self.getArrayCartesianStateByStaticState(self.getFutureStateByAction(self.Action.LEFT))
            futureStateRIGHT = self.getArrayCartesianStateByStaticState(self.getFutureStateByAction(self.Action.RIGHT))
            futureStateDOWN = self.getArrayCartesianStateByStaticState(self.getFutureStateByAction(self.Action.DOWN))

            valPolicyUP = dataState[futureStateUP[0] - 1, futureStateUP[1] - 1]
            valPolicyLEFT = dataState[futureStateLEFT[0] - 1, futureStateLEFT[1] - 1]
            valPolicyRIGHT = dataState[futureStateRIGHT[0] - 1, futureStateRIGHT[1] - 1]
            valPolicyDOWN = dataState[futureStateDOWN[0] - 1, futureStateDOWN[1] - 1]

            # -- Implemented only two type of policy (two direction)
            # Case U
            if (valPolicyUP > valPolicyLEFT) and (valPolicyUP > valPolicyRIGHT) and (valPolicyUP > valPolicyDOWN):
                self.data[x, y] = 1
            # Case L
            elif (valPolicyLEFT > valPolicyUP) and (valPolicyLEFT > valPolicyRIGHT) and (valPolicyLEFT > valPolicyDOWN):
                self.data[x, y] = 2
            # Case R
            elif (valPolicyRIGHT > valPolicyUP) and (valPolicyRIGHT > valPolicyLEFT) and (
                    valPolicyRIGHT > valPolicyDOWN):
                self.data[x, y] = 3
            # Case D
            elif (valPolicyDOWN > valPolicyUP) and (valPolicyDOWN > valPolicyLEFT) and (valPolicyDOWN > valPolicyRIGHT):
                self.data[x, y] = 4
            # Case UL
            elif (valPolicyUP == valPolicyLEFT) and (valPolicyUP > valPolicyRIGHT) and (valPolicyUP > valPolicyDOWN):
                self.data[x, y] = 5
            # Case UR
            elif (valPolicyUP == valPolicyRIGHT) and (valPolicyUP > valPolicyLEFT) and (valPolicyUP > valPolicyDOWN):
                self.data[x, y] = 6
            # Case UD
            elif (valPolicyUP == valPolicyDOWN) and (valPolicyUP > valPolicyLEFT) and (valPolicyUP > valPolicyRIGHT):
                self.data[x, y] = 7
            # Case LR
            elif (valPolicyLEFT == valPolicyRIGHT) and (valPolicyLEFT > valPolicyDOWN) and (
                    valPolicyLEFT > valPolicyUP):
                self.data[x, y] = 8
            # Case LD
            elif (valPolicyLEFT == valPolicyDOWN) and (valPolicyLEFT > valPolicyRIGHT) and (
                    valPolicyLEFT > valPolicyUP):
                self.data[x, y] = 9
            # Case RD
            elif (valPolicyRIGHT == valPolicyDOWN) and (valPolicyRIGHT > valPolicyLEFT) and (
                    valPolicyRIGHT > valPolicyUP):
                self.data[x, y] = 10
            # TODO: Implement others possibilities
            else:
                self.data[x, y] = 15

    def getArrayFutureStateByPolicy(self, policy):
        array = []

        if policy == 1:
            array = [self.getFutureStateByAction(self.Action.UP)]
        elif policy == 2:
            array = [self.getFutureStateByAction(self.Action.LEFT)]
        elif policy == 3:
            array = [self.getFutureStateByAction(self.Action.RIGHT)]
        elif policy == 4:
            array = [self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 5:
            array = [self.getFutureStateByAction(self.Action.UP), self.getFutureStateByAction(self.Action.LEFT)]
        elif policy == 6:
            array = [self.getFutureStateByAction(self.Action.UP), self.getFutureStateByAction(self.Action.RIGHT)]
        elif policy == 7:
            array = [self.getFutureStateByAction(self.Action.UP), self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 8:
            array = [self.getFutureStateByAction(self.Action.LEFT), self.getFutureStateByAction(self.Action.RIGHT)]
        elif policy == 9:
            array = [self.getFutureStateByAction(self.Action.LEFT), self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 10:
            array = [self.getFutureStateByAction(self.Action.RIGHT), self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 11:
            array = [self.getFutureStateByAction(self.Action.UP),
                     self.getFutureStateByAction(self.Action.LEFT),
                     self.getFutureStateByAction(self.Action.RIGHT)]
        elif policy == 12:
            array = [self.getFutureStateByAction(self.Action.UP),
                     self.getFutureStateByAction(self.Action.LEFT),
                     self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 13:
            array = [self.getFutureStateByAction(self.Action.UP),
                     self.getFutureStateByAction(self.Action.RIGHT),
                     self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 14:
            array = [self.getFutureStateByAction(self.Action.LEFT),
                     self.getFutureStateByAction(self.Action.RIGHT),
                     self.getFutureStateByAction(self.Action.DOWN)]
        elif policy == 15:
            array = [self.getFutureStateByAction(self.Action.UP),
                     self.getFutureStateByAction(self.Action.LEFT),
                     self.getFutureStateByAction(self.Action.RIGHT),
                     self.getFutureStateByAction(self.Action.DOWN)]

        return array

    def getActionByPolicy(self, policy):
        array = []

        if policy == 1:
            array = [self.Action.UP]
        elif policy == 2:
            array = [self.Action.LEFT]
        elif policy == 3:
            array = [self.Action.RIGHT]
        elif policy == 4:
            array = [self.Action.DOWN]
        elif policy == 5:
            array = [self.Action.UP, self.Action.LEFT]
        elif policy == 6:
            array = [self.Action.UP, self.Action.RIGHT]
        elif policy == 7:
            array = [self.Action.UP, self.Action.DOWN]
        elif policy == 8:
            array = [self.Action.LEFT, self.Action.RIGHT]
        elif policy == 9:
            array = [self.Action.LEFT, self.Action.DOWN]
        elif policy == 10:
            array = [self.Action.RIGHT, self.Action.DOWN]
        elif policy == 11:
            array = [self.Action.UP,
                     self.Action.LEFT,
                     self.Action.RIGHT]
        elif policy == 12:
            array = [self.Action.UP,
                     self.Action.LEFT,
                     self.Action.DOWN]
        elif policy == 13:
            array = [self.Action.UP,
                     self.Action.RIGHT,
                     self.Action.DOWN]
        elif policy == 14:
            array = [self.Action.LEFT,
                     self.Action.RIGHT,
                     self.Action.DOWN]
        elif policy == 15:
            array = [self.Action.UP,
                     self.Action.LEFT,
                     self.Action.RIGHT,
                     self.Action.DOWN]

        decision = np.random.randint(0, len(array))

        return array[decision]

    def showPolicyInformation(self):
        print("##########################################################")
        print(">> Translation of Policy States")
        print(
            "  1: UP, 2: LEFT, 3: RIGHT, 4: DOWN\n  5: UP/LEFT, 6: UP/RIGHT, 7: UP/DOWN, 8: LEFT/RIGHT\n  9: LEFT/DOWN, 10: RIGHT/DOWN ... 15: UP/RIGHT/LEFT/DOWN")
        print("##########################################################")
