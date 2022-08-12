from Lighter1 import MainLighter, SecondLighter


class CrossRoad:
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
        while self.step < 3:
            if self.start:
                for l in new_road:
                    l.do_step()
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
