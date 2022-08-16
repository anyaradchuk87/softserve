class Lighter:
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

    #def __str__(self):
        #return pass


class MainLighter(Lighter):
    def __init__(self, red=False, yellow=False, green=False):
        Lighter.__init__(self, red, yellow, green)
        self.first = False

    def do_step(self):
        v0 = Viewer(self)
        Viewer.view_lights(v0)
        Lighter.on_red(self)
        v1 = Viewer(self)
        Viewer.view_lights(v1)
        Lighter.on_yellow(self)
        v2 = Viewer(self)
        Viewer.view_lights(v2)
        Lighter.on_green(self)
        v3 = Viewer(self)
        Viewer.view_lights(v3)


class SecondLighter(Lighter):
    def __init__(self, red=False, yellow=False, green=False):
        Lighter.__init__(self, red, yellow, green)
        self.second = True

    def do_step(self):
        v0 = Viewer(self)
        Viewer.view_lights(v0)
        Lighter.on_green(self)
        v1 = Viewer(self)
        Viewer.view_lights(v1)
        Lighter.on_yellow(self)
        v2 = Viewer(self)
        Viewer.view_lights(v2)
        Lighter.on_red(self)
        v3 = Viewer(self)
        Viewer.view_lights(v3)


class Viewer:
    def __init__(self, lighter):
        self.red = lighter.red
        self.yellow = lighter.yellow
        self.green = lighter.green

    def view_lights(self):  # viewer
        if self.red:
            print('R - -')
        elif self.yellow:
            print('- Y -')
        elif self.green:
            print('- - G')
        else:
            print('- - -')
