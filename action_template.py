from mojograsp.simcore.action import Action


class ActionTemplate(Action):

    def __init__(self):
        pass

    def set_action(self):
        self.current_action = {}

    def get_action(self) -> dict:
        return self.current_action
