import random

class Bandit:
    def __init__(self, avg):
        self.avg = avg

    # determining the values of the parameters 
    mu = 100
    sigma = 50
      
    # using the gauss() method 
    print(random.gauss(mu, sigma)) 