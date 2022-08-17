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

probablityOfEachScenario = 1/18
total3 = 0
value3 = 0
for n in range(2,6):
    value3 += probablityOfEachScenario*pow(discountFactor, n-1)
total3 = 4*value3 + 4*probablityOfEachScenario
print(total3)