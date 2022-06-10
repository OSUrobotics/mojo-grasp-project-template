from mojograsp.simcore.replay_buffer import ReplayBuffer, Timestep


class ReplayBufferTemplate(ReplayBuffer):
    def __init__(self):
        pass

    def add_timestep(self, episode_num: int, timestep_num: int):
        pass

    def save_buffer(self, filename: str):
        pass
