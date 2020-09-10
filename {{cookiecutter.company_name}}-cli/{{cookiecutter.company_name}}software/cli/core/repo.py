import os


class Repo:
    def __init__(self, home=None, debug=False):
        if not home:
            self.home = "."
        else:
            self.home = os.path.abspath(home)

        self.debug = debug
