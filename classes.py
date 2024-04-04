import random


class Bandit:
    def __init__(self):
        self.avg = random.gauss(0, 1)

    def play(self):
        return random.gauss(self.avg, 1)


class BanDix:
    def __init__(self):
        self.tab = []
        maxAvg = 0
        maxBanditIndex = 0
        for i in range(10):
            newBandit = Bandit()
            self.tab.append(newBandit)
            if (newBandit.avg > maxAvg):
                maxAvg = newBandit.avg
                maxBanditIndex = i

        self.banditMaxAvg = maxBanditIndex

    def play(self, arm_number):
        if arm_number > 9 or arm_number < 0:
            raise ValueError("Valeur impossible, erreur")
        else:
            return self.tab[arm_number].play()


class GreedyPlayer:

    def __init__(self, n, eps):
        self.n = n
        self.eps = eps
        self.action_values = []
        self.eval_count = []

    def _random_action(self):
        return random.choice(self.action_values)

    def _greedy_action(self):
        best_actions = []
        highest_value = 0

        for i in self.action_values:
            if(self.action_values[i]>highest_value):
                best_actions = []
                best_actions.append(i)
            elif(self.action_values[i]==highest_value):
                best_actions.append(i)
                
        return random.choice(best_actions)

    def get_action(self):
        explore = random.random()
        if explore < self.eps:
            return self._random_action() 
        else:
            return self._greedy_action()
