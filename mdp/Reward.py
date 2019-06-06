from mdp.GridRules import GridRules


class Reward(GridRules):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.name = "REWARD"
