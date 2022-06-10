from mojograsp.simcore.reward import Reward


class RewardTemplate(Reward):

    def __init__(self):
        pass

    def set_reward(self):
        self.current_reward = {}

    def get_reward(self) -> dict:
        return self.current_reward
