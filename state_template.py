from mojograsp.simcore.state import State


class StateTemplate(State):

    def __init__(self):
        pass

    def set_state(self):
        self.current_state = {}

    def get_state(self) -> dict:
        return self.current_state
