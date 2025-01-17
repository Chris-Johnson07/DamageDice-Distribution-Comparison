import numpy as np
import random
import matplotlib.pyplot as plt

attempts = 1000

print('Lets compare damage output.\n')
user_input1 = input('What are we rolling first? (ie 2d6+2d4+5) ')
user_input2 = input('\nWhat are we rolling next? ')

user_damage1 = user_input1.split('+')
user_damage2 = user_input2.split('+')

results1 = []
results2 = []

def rollD(die):
    return random.randint(1,die)

for i in range(attempts):
    #first roll
    attempt_damage1 = 0
    for chunk in user_damage1:
        if 'd' in chunk:
            Dnum, Dtype = chunk.split('d')
            for roll in range(int(Dnum)):
                Dres = rollD(int(Dtype))
                attempt_damage1 += Dres
        else:
            attempt_damage1 += int(chunk)
    results1.append(attempt_damage1)

    #second roll
    attempt_damage2 = 0
    for chunk in user_damage2:
        if 'd' in chunk:
            Dnum, Dtype = chunk.split('d')
            for roll in range(int(Dnum)):
                Dres = rollD(int(Dtype))
                attempt_damage2 += Dres
        else:
            attempt_damage2 += int(chunk)
    results2.append(attempt_damage2)

print('\n')
print('\nAnalysis of {}: '.format(user_input1))
print('Low|', min(results1), '<--', round(np.mean(results1)), '-->', max(results1), '|High')
print('\nAnalysis of {}: '.format(user_input2))
print('Low|', min(results2), '<--', round(np.mean(results2)), '-->', max(results2), '|High')

#plotting
plt.clf()
plt.hist(results1, bins = max(results1)-min(results1), color = 'red', alpha = 0.5, zorder = 3, label = user_input1)
plt.hist(results2, bins = max(results2)-min(results2), color = 'blue', alpha = 0.5, zorder = 3, label = user_input2)
plt.grid(zorder = 0)
plt.xlabel('Amount of Damage')
plt.ylabel('Probability Density')
plt.legend()
plt.show()

