from classes import Bandit, GreedyPlayer, BanDix
import matplotlib.pyplot as plt
from tqdm import tqdm

# bandit1, bandit2, bandit3 = Bandit(), Bandit(), Bandit()
# points1, points2, points3 = [], [], []


tabPointsDesGreedy = [0] * 1000
tableBan10 = []
tableGreedyP = []

nbOfGreedy = 2000
tabPourcentageGreedy = [0] * 1000

for i in range(nbOfGreedy):
    tableBan10.append(BanDix())
    tableGreedyP.append(GreedyPlayer(0.0))
    print([tableBan10[-1].tab[j].avg for j in range(10)])

for i in tqdm(range(1000)):
    for j in range(nbOfGreedy):
        action = tableGreedyP[j].get_action()
        reward = tableBan10[j].play(action)
        tabPointsDesGreedy[i] += reward / nbOfGreedy
        tableGreedyP[j].reward(action, reward)
        if action == tableBan10[j].maxBanditIndex:
            tabPourcentageGreedy[i] += 1 / 20

# Tracer les deux graphiques
fig, axs = plt.subplots(2, 1, figsize=(8, 12))

# Premier graphique pour la moyenne des rewards
axs[0].plot(range(1, 1001), tabPointsDesGreedy, label='Moyenne des rewards des bandits')
axs[0].set_xlabel('i')
axs[0].set_ylabel('moy reward')
axs[0].set_title('Moyenne des rewards des bandits vs. i')
axs[0].legend()

# Deuxième graphique pour le pourcentage greedy
axs[1].plot(range(1, 1001), tabPourcentageGreedy, label='Pourcentage coups optimaux')
axs[1].set_xlabel('i')
axs[1].set_ylabel('Pourcentage')
axs[1].set_title('Pourcentage optimaux vs. i')
axs[1].legend()

# Ajuster l'espacement entre les graphiques
plt.tight_layout()

# Afficher les graphiques
plt.show()
