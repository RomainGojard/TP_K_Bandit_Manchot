import random

class Bandit:
    def __init__(self):
        self.avg = random.gauss(0, 1)

    def play(self):
        return random.gauss(self.avg, 1)

    def je_veux_une_methode_car_je_suis_relou(self, new_avg):
        self.avg = new_avg