import matplotlib.pyplot as plt
import math

def customPlot(Neps, secondVariables, legendPrefix, aggregatedResults, title):
    legends = []
    for secondVariable in secondVariables:
        xAr = []
        yAr = []
        yerr = []
        for Nep in Neps:
            xAr.append(math.log(Nep))
            yAr.append(aggregatedResults[(Nep, secondVariable, 'mean')])
            yerr.append(aggregatedResults[(Nep, secondVariable, 'error')])
        plt.errorbar(xAr, yAr, yerr, fmt = 'o',
            elinewidth = 0, capsize=10)
        plt.xlabel('log(Nep)')
        plt.ylabel('discouted reward') 
        legends.append(legendPrefix + ' = ' + str(secondVariable))
    plt.gca().legend(legends)
    plt.title(title)
    plt.show()

Neps = [10, 100]
epsilons = [0.3, 0.5]

aggregatedResults = {}

aggregatedResults[(10, 0.3, 'mean')] = 1
aggregatedResults[(10, 0.3, 'error')] = 1

aggregatedResults[(100, 0.3, 'mean')] = 4
aggregatedResults[(100, 0.3, 'error')] = 8

aggregatedResults[(10, 0.5, 'mean')] = 9
aggregatedResults[(10, 0.5, 'error')] = 12


aggregatedResults[(100, 0.5, 'mean')] = 1
aggregatedResults[(100, 0.5, 'error')] = 10

# customPlot(Neps, epsilons, 'epsilon', aggregatedResults, 'depende')


