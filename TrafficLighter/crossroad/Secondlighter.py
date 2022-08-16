from Lighter import Lighter
from Mainlighter import MainLighter


class SecondLighter(Lighter):
    def __init__(self, red=False, yellow=False, green=False):
        Lighter.__init__(self, red, yellow, green)
        self.set_red(red)
        self.set_yellow(yellow)
        self.set_green(green)

    def do_step(self):
        if MainLighter.get_red(self):
            self.set_red(Lighter.SECOND_LIGHTS[Lighter.state][0])
            self.set_yellow(Lighter.SECOND_LIGHTS[Lighter.state][1])
            self.set_green(Lighter.SECOND_LIGHTS[Lighter.state][2])
