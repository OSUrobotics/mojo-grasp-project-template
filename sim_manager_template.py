from mojograsp.simcore.sim_manager import SimManager

# Only use a custom SimManager class if you know what you are doing.
# It will break things if not done correctly.


class SimManagerTemplate(SimManager):
    def __init__(self):
        pass

    def add_phase(self):
        pass

    def run(self):
        pass

    def stall(self):
        super().stall()
