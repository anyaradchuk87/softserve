from Mainlighter import MainLighter


class Duplicate(MainLighter):
    def __init__(self, lighter):
        MainLighter.__init__(self) #
        self.lighter = lighter

    def do_step(self):
        self.set_red(self.lighter.get_red())
        self.set_yellow(self.lighter.get_yellow())
        self.set_green(self.lighter.get_green())
