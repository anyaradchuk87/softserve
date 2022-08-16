class Lighter:
    MAIN_LIGHTS = [(True, False, False), (False, True, False), (False, False, True), (False, True, False)]

    SECOND_LIGHTS = [(False, False, True), (False, True, False), (True, False, False), (False, True, False)]
    state = 0

    def __init__(self, red=False, yellow=False, green=False):
        self.__red = red
        self.__yellow = yellow
        self.__green = green

    def __str__(self):
        return f'{self.__red:3}{self.__yellow:3}{self.__green:3}'

    def set_red(self, red):
        self.__red = red

    def get_red(self):
        return self.__red

    def set_yellow(self, yellow):
        self.__yellow = yellow

    def get_yellow(self):
        return self.__yellow

    def set_green(self, green):
        self.__green = green

    def get_green(self):
        return self.__green

    def do_step(self):
        pass

