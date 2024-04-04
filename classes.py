import random


class Bandit:
    def __init__(self):
        self.avg = random.gauss(0, 1)

    def play(self):
        return random.gauss(self.avg, 1)


class BanDix:
    def __init__(self):
        self.tab = []
        for i in range(10):
            self.tab.append(Bandit())

