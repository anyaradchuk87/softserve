from Lighter import Lighter


class MainLighter(Lighter):
    def __init__(self, red=True, yellow=False, green=False):
        Lighter.__init__(self, red, yellow, green)

    def do_step(self):
        self.set_red(Lighter.MAIN_LIGHTS[Lighter.state][0])
        self.set_yellow(Lighter.MAIN_LIGHTS[Lighter.state][1])
        self.set_green(Lighter.MAIN_LIGHTS[Lighter.state][2])
