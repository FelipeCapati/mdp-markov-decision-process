import numpy as np
from enum import Enum
import math


class GridRules:
    def __init__(self, x, y):
        self.name = ""
        self.dimX = x
        self.dimY = y
        self.stateNow = 1
        self.arrayState = np.arange(1, x * y + 1)
        self.data = np.zeros([x, y])

    class Action(Enum):
        UP = 1
        LEFT = 2
        RIGHT = 3
        DOWN = 4

    def _getCartesianStateY(self, state):
        return math.ceil(state / self.dimX)

    def _getCartesianStateX(self, state):
        return state % self.dimX if state % self.dimX else self.dimX

    def getStaticStateByCartesianState(self, x, y):
        return self.dimX * (y - 1) + x

    def getDataByStaticState(self, state):
        return self.data[self._getCartesianStateX(state) - 1, self._getCartesianStateY(state) - 1]

    def getArrayCartesianStateByStaticState(self, state):
        return [self._getCartesianStateX(state), self._getCartesianStateY(state)]

    def getArrayCartesianStateByStateNow(self):
        return [self._getCartesianStateX(self.stateNow), self._getCartesianStateY(self.stateNow)]

    def setStateNowByCartesianState(self, x, y):
        self.stateNow = self.dimX * (y - 1) + x

    def getFutureStateByAction(self, action):
        pos = self.getArrayCartesianStateByStateNow()
        x = 0
        y = 1

        futureState = 0

        if ((pos[x] == 1 and action == self.Action.LEFT) or
                (pos[x] == self.dimX and action == self.Action.RIGHT) or
                (pos[y] == 1 and action == self.Action.UP) or
                (pos[y] == self.dimY and action == self.Action.DOWN)):
            futureState = self.stateNow
        else:
            if action == self.Action.UP:
                futureState = self.getStaticStateByCartesianState(pos[x], pos[y] - 1)

            elif action == self.Action.LEFT:
                futureState = self.getStaticStateByCartesianState(pos[x] - 1, pos[y])

            elif action == self.Action.RIGHT:
                futureState = self.getStaticStateByCartesianState(pos[x] + 1, pos[y])

            elif action == self.Action.DOWN:
                futureState = self.getStaticStateByCartesianState(pos[x], pos[y] + 1)

        return futureState

    def showCMD(self):
        print("%s TABLE" % self.name)
        linePrint = " "
        for x in range(len(self.data)):
            linePrint = linePrint + "_____"
        print(linePrint)
        for x in range(len(self.data)):
            linePrint = "|"
            for y in range(len(self.data[x])):
                if self.data[x, y] <= -10:
                    linePrint = linePrint + "" + str(self.data[x, y]) + "|"
                elif self.data[x, y] > -10 and self.data[x, y] < 0:
                    linePrint = linePrint + " " + str(self.data[x, y]) + "|"
                elif self.data[x, y] >= 0 and self.data[x, y] < 10:
                    linePrint = linePrint + "  " + str(self.data[x, y]) + "|"
                elif self.data[x, y] >= 10:
                    linePrint = linePrint + " " + str(self.data[x, y]) + "|"
            print(linePrint)
        print("")
