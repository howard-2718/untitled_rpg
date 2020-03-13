class StateMachine(object):

    def __init__(self):
        self.state = 'title'
        self.cur_menu = None
        self.cur_map = None
        self.cur_battle = None

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
