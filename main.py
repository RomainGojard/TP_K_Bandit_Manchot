from classes import Bandit
import matplotlib.pyplot as plt

bandit = Bandit()
avg_points = []  # Liste pour stocker les points avg

for i in range(1000):
    bandit.je_veux_une_methode_car_je_suis_relou(bandit.play())
    avg_points.append(bandit.avg)  # Ajouter avg à la liste
    print(bandit.avg)

# Tracer le graphique
plt.plot(range(1, 1001), avg_points, label='Avg Points')
plt.xlabel('i')
plt.ylabel('Avg Points')
plt.title('Avg Points vs. i')
plt.legend()
plt.show()
