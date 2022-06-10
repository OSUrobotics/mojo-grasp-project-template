from mojograsp.simcore.environment import Environment


class EnvironmentTemplate(Environment):
    def __init__(self):
        pass

    def setup(self):
        pass

    def step(self):
        super().step()

    def reset(self):
        pass
