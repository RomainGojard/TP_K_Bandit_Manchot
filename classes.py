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

    def __str__(self):
        print("max avg", self.banditMaxAvg, "\n")
        print()


class GreedyPlayer:

    def __init__(self, eps, n=10):
        self.n = n
        self.eps = eps
        self.action_values = [0] * n
        self.eval_count = [0] * n

    def _random_action(self):
        return random.randint(0, 9)

    def _greedy_action(self):
        best_actions = []
        highest_value = 0

        for i in range(len(self.action_values)):
            if (self.action_values[i] > highest_value):
                best_actions = []
                best_actions.append(i)
            elif (self.action_values[i] == highest_value):
                best_actions.append(i)

        return random.choice(best_actions)

    def reward(self, action, reward):
        self.action_values[action] += reward
        self.eval_count[action] += 1

    def get_action(self):
        explore = random.random()
        if explore < self.eps:
            return self._random_action()
        else:
            return self._greedy_action()

    def __str__(self):
        print("n", self.n, "\n")
        print("eps", self.eps, "\n")
        print("action values", self.action_values, "\n")
        print("eval count", self.eval_count, "\n")
