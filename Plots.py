import matplotlib.pyplot as plt
import math

def customPlot(Neps, epsilons, aggregatedResults, title):
    for epsilon in epsilons:
        xAr = []
        yAr = []
        yerr = []
        for Nep in Neps:
            xAr.append(math.log(Nep))
            yAr.append(aggregatedResults[(epsilon, Nep, 'mean')])
            yerr.append(aggregatedResults[(epsilon, Nep, 'error')])
        plt.errorbar(xAr, yAr, yerr)
        plt.xlabel('log(Nep)')
        plt.ylabel('discouted reward')
        plt.title(title + ', epsilon=' + str(epsilon))
        plt.show()

Neps = [10, 100]
epsilons = [0.3, 0.5]

aggregatedResults = {}

aggregatedResults[(0.3, 10, 'mean')] = 1
aggregatedResults[(0.3, 10, 'error')] = 1

aggregatedResults[(0.3, 100, 'mean')] = 4
aggregatedResults[(0.3, 100, 'error')] = 8

aggregatedResults[(0.5, 10, 'mean')] = 9
aggregatedResults[(0.5, 10, 'error')] = 12


aggregatedResults[(0.5, 100, 'mean')] = 1
aggregatedResults[(0.5, 100, 'error')] = 10

# customPlot(Neps, epsilons, aggregatedResults, 'depende')


