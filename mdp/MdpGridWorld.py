from mdp.Policy import Policy
from mdp.Reward import Reward
from mdp.State import State
import numpy as np

class MdpGridWorld:
    def __init__(self):
        pass

    def policyEvaluation(self, r: Reward, S: State, pi: Policy, k=100, gama=0.01, teta=0.000001, nRound=5):
        piLine = Policy(pi.dimX, pi.dimY)
        X = 0
        Y = 1

        print("****************************************")
        print("*** INITIAL LOOP TO GET POLICY TABLE ***")
        print("****************************************")
        numberOfIterations = 0
        while k > 0:
            # Do - While emulation
            while True:
                deltaMax = 0
                for s in S.arrayState:
                    S.stateNow = s
                    pi.stateNow = s

                    # -- v <- V(s)
                    pos = S.getArrayCartesianStateByStateNow()
                    v = S.data[pos[X] - 1, pos[Y] - 1]

                    # -- V(s) <- Markov equation for probability 1
                    arrayState = pi.getArrayFutureStateByPolicy(pi.data[pos[X] - 1, pos[Y] - 1])

                    auxSum = 0
                    for state in arrayState:
                        auxSum = auxSum + r.getDataByStaticState(S.stateNow) + gama * S.getDataByStaticState(state)
                    S.data[pos[X] - 1, pos[Y] - 1] = auxSum/len(arrayState)
                    vLinha = auxSum/len(arrayState)

                    delta = v - vLinha

                    deltaMax = delta if delta > deltaMax else deltaMax

                numberOfIterations += 1

                S.showCMD()

                ## -- Until delta < Teta (a small positive number)
                if deltaMax < teta:
                    break

            S.showCMD()

            # -- 3. Policy Improvement
            pi.stable = True
            piLine.policyUpdateByState(S.data)

            for s in S.arrayState:
                S.stateNow = s

                # -- v <- V(s)
                pos = S.getArrayCartesianStateByStateNow()
                y = pos[0] - 1
                x = pos[1] - 1

                b = pi.data[x][y]

                if b != piLine.data[x][y]:
                    pi.stable = False

            pi.policyUpdateByState(S.data)
            pi.showCMD()

            if pi.stable == True:
                break

            k -= 1

        print("****************************")
        print("*** END SOLUTION PROCESS ***")
        print("****************************")

        print("Number of Iterations: %s" %(numberOfIterations))

        r.showCMD()
        S.showCMD()
        pi.showCMD()
        pi.showPolicyInformation()

        return [r, S, pi]


    def valueIteraction(self, r, S, pi, gama=0.01, teta=0.000000001, nRound=8):
        print("****************************************")
        print("*** INITIAL LOOP TO GET POLICY TABLE ***")
        print("****************************************")
        numberOfIterations = 0
        X = 0
        Y = 1
        # Do - While emulation
        while True:
            deltaMax = 0
            for s in S.arrayState:
                S.stateNow = s

                # -- v <- V(s)
                pos = S.getArrayCartesianStateByStateNow()
                v = S.data[pos[X] - 1, pos[Y] - 1]

                # -- V(s) <- Markov equation for probability 1
                futureStateUP = S.getFutureStateByAction(S.Action.UP)
                futureStateLEFT = S.getFutureStateByAction(S.Action.LEFT)
                futureStateRIGHT = S.getFutureStateByAction(S.Action.RIGHT)
                futureStateDOWN = S.getFutureStateByAction(S.Action.DOWN)

                S.data[pos[X] - 1, pos[Y] - 1] = round(np.amax([
                    r.getDataByStaticState(S.stateNow) + gama * S.getDataByStaticState(futureStateUP),
                    r.getDataByStaticState(S.stateNow) + gama * S.getDataByStaticState(futureStateLEFT),
                    r.getDataByStaticState(S.stateNow) + gama * S.getDataByStaticState(futureStateRIGHT),
                    r.getDataByStaticState(S.stateNow) + gama * S.getDataByStaticState(futureStateDOWN)])
                    , nRound)
                vLinha = S.data[pos[X] - 1, pos[Y] - 1]

                delta = v - vLinha

                deltaMax = delta if delta > deltaMax else deltaMax

            numberOfIterations += 1

            S.showCMD()

            ## -- Until delta < Teta (a small positive number)
            if deltaMax < teta:
                break

        # -- Update Policy Table
        pi.policyUpdateByState(S.data)

        print("****************************")
        print("*** END SOLUTION PROCESS ***")
        print("****************************")

        print("Number of Iterations: %s" %(numberOfIterations))

        r.showCMD()
        S.showCMD()
        pi.showCMD()
        pi.showPolicyInformation()

        return [r, S, pi]
