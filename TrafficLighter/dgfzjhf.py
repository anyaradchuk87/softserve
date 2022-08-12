import time


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


class Viewer:
    def __init__(self, lighter):
        self.red = lighter.red
        self.yellow = lighter.yellow
        self.green = lighter.green

    def view_lights(self):  # viewer
        if self.red:
            print('* - -')
        elif self.yellow:
            print('- * -')
        elif self.green:
            print('- - *')
        else:
            print('- - -')


class Controller:
    start = True
    RED_TIME = 3
    YELLOW_TIME = 1
    GREEN_TIME = 3
    step = 0

    def __init__(self, lighter):
        self.red = lighter.red
        self.yellow = lighter.yellow
        self.green = lighter.green
        self.step = lighter.step
        self.stop = lighter.stop

    def do_lights(self):  # controller
        Viewer.view_lights(tr_light)
        while self.step < 3:
            if self.start:
                time.sleep(Controller.YELLOW_TIME)
                Lighter.on_red(tr_light)
                Viewer.view_lights(tr_light.red)
                time.sleep(Controller.RED_TIME)
                Lighter.on_yellow(tr_light)
                Viewer.view_lights(tr_light.yellow)
                time.sleep(Controller.YELLOW_TIME)
                Lighter.on_green(tr_light)
                Viewer.view_lights(tr_light.green)
                time.sleep(Controller.GREEN_TIME)
                Lighter.on_yellow(tr_light)
                Viewer.view_lights(tr_light.yellow)
                time.sleep(Controller.YELLOW_TIME)
            self.step += 1
        self.start = False


tr_light = Lighter()
run = Controller(tr_light)
run.do_lights()
