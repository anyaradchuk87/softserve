import time


class Lighter:
    def __init__(self, red=False, yellow=False, green=False):
        self.red = red
        self.yellow = yellow
        self.green = green


class Controller:
    def __init__(self, red=False, yellow=False, green=False):
        self.red = red
        self.yellow = yellow
        self.green = green

    def on_red(self):
        self.red = True
        self.yellow = False
        self.green = False

    def on_yellow(self):
        self.red = False
        self.yellow = True
        self.green = False

    def on_green(self):
        self.red = False
        self.yellow = False
        self.green = True


class Viewer:
    pass
