import time


class TrafficLight:
    stop = True
    RED_TIME = 3
    YELLOW_TIME = 1
    GREEN_TIME = 3
    step = 0

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

    def view_lights(self):
        if self.red:
            print('* - -')
        elif self.yellow:
            print('- * -')
        elif self.green:
            print('- - *')
        else:
            print('- - -')

    def do_lights(self):
        self.view_lights()
        while self.step < 3:
            if self.stop:
                time.sleep(self.YELLOW_TIME)
                self.on_red()
                self.view_lights()
                time.sleep(self.RED_TIME)
                self.on_yellow()
                self.view_lights()
                time.sleep(self.YELLOW_TIME)
                self.on_green()
                self.view_lights()
                time.sleep(self.GREEN_TIME)
                self.on_yellow()
                self.view_lights()
                time.sleep(self.YELLOW_TIME)
            self.step += 1
        self.stop = False


tr_light = TrafficLight()

tr_light.do_lights()
