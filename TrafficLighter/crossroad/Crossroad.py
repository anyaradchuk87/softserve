from Lighter import Lighter
from Mainlighter import MainLighter
from Secondlighter import SecondLighter


class CrossRoad:

    @staticmethod
    def show_header():
        print('\tMain \t Second \t Duplic \t Second')

    @staticmethod
    def show_lighter(lighter):
        print(lighter, end='\t')

    def __init__(self):
        self.road = []
        self.current_position = 0
        self.step = 0
        self.start = True

    def add_lighter(self, lighter):
        self.road.append(lighter)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_position >= len(self.road):
            self.current_position = 0
            raise StopIteration

        current_lighter = self.road[self.current_position]
        self.current_position += 1

        return current_lighter

    def run(self):
        CrossRoad.show_header()
        while self.step < 7:
            if self.start:
                for l in new_road:
                    if Lighter.state < 4:
                        l.do_step()
                        CrossRoad.show_lighter(l)
                        Lighter.state += 1
                    else:
                        Lighter.state = 0
                print('------------')
            self.step += 1
        self.start = False


l1 = MainLighter()
l2 = SecondLighter()
l3 = MainLighter()
l4 = SecondLighter()

new_road = CrossRoad()
new_road.add_lighter(l1)
new_road.add_lighter(l2)
new_road.add_lighter(l3)
new_road.add_lighter(l4)

new_road.run()
