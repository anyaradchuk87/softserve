class TrafficLights:

    def __init__(self, green, yellow, red):
        self.green = green
        self.yellow = yellow
        self.red = red

    def run(self, forward):
        self.print_traffic_light()
        for i in range(2):
            if forward:
                if self.green:
                    self.red = False
                    self.yellow = True
                    self.green = False

                elif self.red or self.yellow:
                    self.red = True
                    self.yellow = False
                    self.green = False

            else:
                if self.yellow or self.green:
                    self.red = False
                    self.yellow = False
                    self.green = True

                elif self.red:
                    self.red = False
                    self.yellow = True
                    self.green = False
            self.print_traffic_light()

    def print_traffic_light(self):
        print('*' if self.green else '-',
              '*' if self.yellow else '-',
              '*' if self.red else '-')

traffic_light = TrafficLights(True, False, False)
traffic_light.run(True)
traffic_light.run(False)
