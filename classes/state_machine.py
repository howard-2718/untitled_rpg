class StateMachine(object):

    def __init__(self):
        self.state = 'title'

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
