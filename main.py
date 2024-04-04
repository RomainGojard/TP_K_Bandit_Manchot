from classes import Bandit, GreedyPlayer, BanDix
import matplotlib.pyplot as plt
from tqdm import tqdm

# bandit1, bandit2, bandit3 = Bandit(), Bandit(), Bandit()
# points1, points2, points3 = [], [], []


"""
for i in range(1000):
    value1, value2, value3 = bandit1.play(), bandit2.play(), bandit3.play()
    points1.append(value1)
    points2.append(value2)
    points3.append(value3)
    print(value1, value2, value3)

# Créer trois sous-graphiques
fig, axs = plt.subplots(3, 1, figsize=(8, 12))

# bandit1
axs[0].plot(range(1, 1001), points1, label='Bandit 1')
axs[0].set_xlabel('i')
axs[0].set_ylabel('value')
axs[0].set_title('Bandit 1 - Value vs. i')
axs[0].legend()

# bandit2
axs[1].plot(range(1, 1001), points2, label='Bandit 2')
axs[1].set_xlabel('i')
axs[1].set_ylabel('value')
axs[1].set_title('Bandit 2 - Value vs. i')
axs[1].legend()

# bandit3
axs[2].plot(range(1, 1001), points3, label='Bandit 3')
axs[2].set_xlabel('i')
axs[2].set_ylabel('value')
axs[2].set_title('Bandit 3 - Value vs. i')
axs[2].legend()

# Ajuster l'espacement entre les graphiques
plt.tight_layout()

# Afficher les graphiques
plt.show()

"""

tabPointsDesGreedy = [0] * 1000
tableBan10 = []
tableGreedyP = []

nbOfGreedy = 2000

for i in range(nbOfGreedy):
    tableBan10.append(BanDix())
    tableGreedyP.append(GreedyPlayer(0.1))
    print([tableBan10[-1].tab[j].avg for j in range(10)])

for i in tqdm(range(1000)):
    for j in range(nbOfGreedy):
        action = tableGreedyP[j].get_action()
        reward = tableBan10[j].play(action)
        tabPointsDesGreedy[i] += reward / nbOfGreedy
        tableGreedyP[j].reward(action, reward)

for j in range(10):
    tableBan10[j].__str__()
    tableGreedyP[j].__str__()

# Tracer le graphique avec les trois courbes
plt.plot(range(1, 1001), tabPointsDesGreedy, label='Moyenne des rewards des bandits')
plt.xlabel('i')
plt.ylabel('moy reward')
plt.title('moy reward vs. i')
plt.legend()
plt.show()

'''
# Créer 1 sous-graphique
fig, axs = plt.subplots(1, 1, figsize=(8, 12))

axs.plot(range(1, 1001), points, label='Rewards')
axs.set_xlabel('i')
axs.set_ylabel('value')
axs.set_title('Rewards')
axs.legend()

# Afficher les graphiques
plt.show()
'''
