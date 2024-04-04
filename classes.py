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

    def play(self, arm_number):
        if arm_number > 9 or arm_number < 0:
            raise ValueError("Valeur impossible, erreur")
        else:
            return self.tab[arm_number].play()

