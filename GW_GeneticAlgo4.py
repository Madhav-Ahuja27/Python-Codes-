from deap import base
from deap import creator
from deap import tools
from deap import algorithms
import numpy as np
import random
import numpy

import matplotlib.pyplot as plt



class Knapsack:

    def __init__(self):

        # initialize instance variables:
        self.items = []
        self.maxCapacity = 0

        # initialize the data:
        self.__initData()

    def __len__(self):

        return len(self.items)

    def __initData(self):

        self.items = [
            ("map", 9, 150),
            ("compass", 13, 35),
            ("water", 153, 200),
            ("sandwich", 50, 160),
            ("glucose", 15, 60),
            ("tin", 68, 45),
            ("banana", 27, 60),
            ("apple", 39, 40),
            ("cheese", 23, 30),
            ("beer", 52, 10),
            ("suntan cream", 11, 70),
            ("camera", 32, 30),
            ("t-shirt", 24, 15),
            ("trousers", 48, 10),
            ("umbrella", 73, 40),
            ("waterproof trousers", 42, 70),
            ("waterproof overclothes", 43, 75),
            ("note-case", 22, 80),
            ("sunglasses", 7, 20),
            ("towel", 18, 12),
            ("socks", 4, 50),
            ("book", 30, 10)
        ]

        self.maxCapacity = 400

    def getValue(self, individual):

      totalValue = totalWeight = 0
      for i in range(len(individual)):
          if individual[i] == 1:
              totalValue += self.items[i][2]  # Add the value of the selected item
              totalWeight += self.items[i][1]  # Add the weight of the selected item
      return totalValue




    def printItems(self, zeroOneList):

        totalWeight = totalValue = 0

        for i in range(len(zeroOneList)):
          #  if zeroOneList[i] == 1:
          #   item, weight, value = self.items[i]
          #   totalWeight += weight
          #   totalValue += value
          _,weight,value=individual[i]
          if totalWeight + weight <self.maxCapacity:
            totalWeight+=weight*individual[i]
            totalValue+=value*individual[i]

        print(f"- Adding {item}: weight = {weight}, value = {value}, accumulated weight = {totalWeight}, accumulated value = {totalValue}")
        print(f"- Total weight = {totalWeight}, Total value = {totalValue}")


        print("- Adding {}: weight = {}, value = {}, accumulated weight = {}, accumulated value = {}".format(item, weight, value, totalWeight, totalValue))
        print("- Total weight = {}, Total value = {}".format(totalWeight, totalValue))


knapsack = Knapsack()


import numpy as np
import matplotlib.pyplot as plt
import random
from deap import base, tools, creator, algorithms

popSize = 1100
generations = 1100
chromSize = 7 * 3 * 8
pCX = 0.99
pMut = 0.1

random.seed(42)

## Set up toolbox

toolbox = base.Toolbox()
toolbox.register('binary', random.randint,0,1)


creator.create('fitnessmax', base.Fitness,weights=(-1.0,))
creator.create('Individual',list,
               fitness = creator.fitnessmax)
toolbox.register('createIndividual',tools.initRepeat,
                creator.Individual, toolbox.binary,
                len(guard))
toolbox.register('createPop',tools.initRepeat, list,
                 toolbox.createIndividual)


def fitnessFunction(individual):
   return Knapsack.getValue(individual,),

## registering the evolutionary operators
toolbox.register('evaluate', fitnessFunction)
toolbox.register('select', tools.selTournament,
 tournsize=3)
# toolbox.register('select', tools.selRoulette)
toolbox.register('mate', tools.cxUniform,indpb=0.3)
toolbox.register('mutate', tools.mutShuffleIndexes,
indpb=1/chromSize)

startingPop = toolbox.createPop(popSize)
stats = tools.Statistics(lambda ind:ind.fitness.values)
stats.register('max', np.max)
stats.register('avg', np.mean)

hof = tools.HallOfFame(5)

finalPop, logbook = eaSimpleWithElitism(
    startingPop,
    toolbox,
    pCX,
    pMut,
    generations,
    stats,
    hof,
    True
)

max, avg = logbook.select('max','avg')

plt.plot(max, color='red')
plt.plot(avg, color='green')
plt.ylabel('max/avg fitness per generation')
plt.xlabel('generation')
plt.show()

best = hof[0]

guard.Knapsack.printItems(best)
