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


class MainLighter(Lighter):
    def __init__(self, red=False, yellow=False, green=False):
        Lighter.__init__(self, red, yellow, green)
        self.first = False

    def view_light(self):
        if self.red:
            print('R - -')
        elif self.yellow:
            print('- Y -')
        elif self.green:
            print('- - G')
        else:
            print('- - -')

    def do_step(self):
        Lighter.on_red(self)
        self.view_light()
        Lighter.on_yellow(self)
        self.view_light()
        Lighter.on_green(self)
        self.view_light()
        Lighter.on_yellow(self)
        self.view_light()


class SecondLighter(Lighter):
    def __init__(self, red=False, yellow=False, green=False):
        Lighter.__init__(self, red, yellow, green)
        self.second = True

    def view_light(self):
        if self.red:
            print('- - R')
        elif self.yellow:
            print('- Y -')
        elif self.green:
            print('G - -')
        else:
            print('- - -')

    def do_step(self):
        Lighter.on_green(self)
        self.view_light()
        Lighter.on_yellow(self)
        self.view_light()
        Lighter.on_red(self)
        self.view_light()
        Lighter.on_yellow(self)
        self.view_light()
