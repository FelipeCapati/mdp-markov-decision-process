import pytest
from mdp.MdpGridWorld import MdpGridWorld
from mdp.Policy import Policy
from mdp.Reward import Reward
from mdp.State import State
import numpy as np

def test_mdp_valueIteraction():
    ###########
    # Arranje #
    ###########

    # -- Initialize Constants
    GAMA = 0.9
    TETA = 0.000001
    ROUND = 5

    # -- Initialize Dimension about Small Grid Word
    dimX = 4
    dimY = 4

    # -- Initilize states and actions
    S = State(dimX, dimY)
    S.showCMD()

    # -- Initialize r(s,a)
    r = Reward(dimX, dimY)
    r.data = np.ones([dimX, dimY]) * -1
    r.data[0, 0] = 0
    r.data[3, 3] = 0
    r.showCMD()

    # -- Initialize Policy Class
    pi = Policy(dimX, dimY)
    pi.showCMD()

    Mdp = MdpGridWorld()

    ###########
    #   Act   #
    ###########
    # -- 3. Value Iteraction (Uncomment this block code)
    [r, S, pi] = Mdp.valueIteraction(r, S, pi, gama=GAMA, teta=TETA, nRound=ROUND)


    ###########
    #  Assert #
    ###########
    validation = np.array([[5., 2., 2., 9.], [1., 5., 15., 4.], [1., 15., 10., 4.], [6., 3., 3., 10.]])
    assert np.array_equal(pi.data, validation), "Test Failed"


def test_mdp_policyEvaluation():
    ###########
    # Arranje #
    ###########

    # -- Initialize Constants
    GAMA = 0.9
    TETA = 0.000001
    ROUND = 5

    # -- Initialize Dimension about Small Grid Word
    dimX = 4
    dimY = 4

    # -- Initilize states and actions
    S = State(dimX, dimY)
    S.showCMD()

    # -- Initialize r(s,a)
    r = Reward(dimX, dimY)
    r.data = np.ones([dimX, dimY]) * -1
    r.data[0, 0] = 0
    r.data[3, 3] = 0
    r.showCMD()

    # -- Initialize Policy Class
    pi = Policy(dimX, dimY)
    pi.showCMD()

    Mdp = MdpGridWorld()

    ###########
    #   Act   #
    ###########
    # -- 3. Value Iteraction (Uncomment this block code)
    [r, S, pi] = Mdp.policyEvaluation(r, S, pi, gama=GAMA, teta=TETA, nRound=ROUND)


    ###########
    #  Assert #
    ###########
    validation = np.array([[5., 2., 2., 2.], [1., 5., 4., 4.], [1., 3., 10., 4.], [1., 3., 3., 10.]])
    assert np.array_equal(pi.data, validation), "Test Failed"
