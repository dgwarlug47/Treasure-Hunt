# question a
probablityOfEachScenario = 1/24
discountFactor = 0.95

total = 0
for n in range(1,25):
    total += probablityOfEachScenario*pow(discountFactor, n-1)
print(total)

probablityOfEachScenario = 1/18
total2 = 0
for n in range(1,6):
    total2 += probablityOfEachScenario*pow(discountFactor, n-1)
print(total2)