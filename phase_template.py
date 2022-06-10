from mojograsp.simcore.phase import Phase


class PhaseTemplate(Phase):

    def __init__(self):
        pass

    def setup(self):
        pass

    def execute_action(self):
        pass

    def exit_condition(self) -> bool:
        return True

    def next_phase(self) -> str:
        return None

    def pre_step(self):
        pass

    def post_step(self):
        pass
