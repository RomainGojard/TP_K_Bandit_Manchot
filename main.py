from classes import Bandit, GreedyPlayer, BanDix
import matplotlib.pyplot as plt
from tqdm import tqdm

nbTabTabGreedy = 3
nbOfGreedy = 2000
tabPointsDesGreedy = [[0] * 1000 for _ in range(nbTabTabGreedy)]
tableTableBan10 = [[] for _ in range(nbTabTabGreedy)]
tableTableGreedy = [[] for _ in range(nbTabTabGreedy)]
tabTabPourcentageGreedy = [[0] * 1000 for _ in range(nbTabTabGreedy)]

for k in range(nbTabTabGreedy):
    for i in range(nbOfGreedy):
        tableTableBan10[k].append(BanDix())
        if k == 0:
            eps = 0
        elif k == 1:
            eps = 0.01
        else:
            eps = 0.1
        tableTableGreedy[k].append(GreedyPlayer(eps))

for i in tqdm(range(1000)):
    for k in range(nbTabTabGreedy):
        for j in range(nbOfGreedy):
            action = tableTableGreedy[k][j].get_action()
            reward = tableTableBan10[k][j].play(action)
            tabPointsDesGreedy[k][i] += reward / nbOfGreedy
            tableTableGreedy[k][j].reward(action, reward)
            if action == tableTableBan10[k][j].maxBanditIndex:
                tabTabPourcentageGreedy[k][i] += 1 / (nbOfGreedy / 100)

# Tracer les deux graphiques
fig, axs = plt.subplots(2, 1, figsize=(8, 12))

# Premier graphique pour la moyenne des rewards
for k in range(nbTabTabGreedy):
    axs[0].plot(range(1, 1001), tabPointsDesGreedy[k], label=f'Greedy {k+1}')
axs[0].set_xlabel('i')
axs[0].set_ylabel('moy reward')
axs[0].set_title('Moyenne des rewards des bandits Greedy vs. i')
axs[0].legend()

# Deuxième graphique pour le pourcentage
for k in range(nbTabTabGreedy):
    axs[1].plot(range(1, 1001), tabTabPourcentageGreedy[k], label=f'Greedy {k+1}')
axs[1].set_xlabel('i')
axs[1].set_ylabel('Pourcentage')
axs[1].set_title('Pourcentage de coups optimaux des bandits Greedy vs. i')
axs[1].legend()

# Ajuster l'espacement entre les graphiques
plt.tight_layout()

# Afficher les graphiques
plt.show()
