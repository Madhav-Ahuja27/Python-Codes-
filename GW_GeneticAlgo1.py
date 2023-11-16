import numpy as np
import matplotlib.pyplot as plt
import random
from deap import base,tools,creator,algorithms
#base contains classes
#creator is used to create classes
#algorithms contains algos to run

##define GA parameters
popSize=100
generations=100
chromSize=100
prob_crossover=0.9
prob_mutation=0.1

random.seed(42)

##set up toolbox
toolbox=base.Toolbox()
toolbox.register('binary',random.randint,0,1)
creator.create('fitnessMax',base.Fitness,weights=(1.0,))
creator.create('Individual',list,fitness=creator.fitnessMax)
toolbox.register('createIndividual',tools.initRepeat,creator.Individual,toolbox.binary,chromSize)
toolbox.register('createPop',tools.initRepeat,list,toolbox.createIndividual)

def fitnessFunction(individual):
    return sum(individual)

##registering the evolutionary operators
toolbox.register('evaluate',fitnessFunction)
toolbox.register('select',tools.selTournament,tournSize=3)
toolbox.register('mate',tools.cxTwoPoint)
toolbox.register('mutate',tools.mutFlipBit,indPb=1/chromSize)

startingPop=toolbox.createPop(popSize)
stats=tools.Statistics(lambda ind:ind.fitness.values)
stats.register('max',np.max)
stats.register('avg',np.mean)
hof=tools.HallOfFame(5)

finalPop,logbook=algorithms.eaSimple(startingPop,
                                     toolbox,
                                     prob_crossover,
                                     prob_mutation,
                                     generations,stats,
                                     hof,
                                     True)
#each line of algo = True, just final output = False

max,avg=logbook.select('max','avg')
plt.plot(max,color='red')
plt.plot(avg,color='green')
plt.xlabel('generation')
plt.ylable('max/avg fitness per generation')
plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
# import random
# from deap import base, tools, creator, algorithms

# ##define GA parameters
# popSize = 1000
# generations = 100
# chromSize = 100
# pCX = 0.9
# pMut = 0.1

# random.seed(42)

# ## Set up toolbox

# toolbox = base.Toolbox()
# toolbox.register('binary', random.randint,0,1)
# creator.create('fitnessMax', base.Fitness,weights=(1.0,))
# creator.create('Individual',list,
#                fitness = creator.fitnessMax)
# toolbox.register('createIndividual',tools.initRepeat,
#                 creator.Individual, toolbox.binary,
#                 chromSize)
# toolbox.register('createPop',tools.initRepeat, list,
#                  toolbox.createIndividual)
                 


# def fitnessFunction(individual):
#    return sum(individual), 
   
#    ## registering the evolutionary operators
# toolbox.register('evaluate', fitnessFunction)
# toolbox.register('select', tools.selTournament,
#  tournsize=3)
# toolbox.register('mate', tools.cxTwoPoint)
# toolbox.register('mutate', tools.mutFlipBit,
# indpb=1/chromSize)

# startingPop = toolbox.createPop(popSize)
# stats = tools.Statistics(lambda ind:ind.fitness.values)
# stats.register('max', np.max)
# stats.register('avg', np.mean)

# hof = tools.HallOfFame(5)

# finalPop, logbook = algorithms.eaSimple(
#     startingPop,
#     toolbox,
#     pCX,
#     pMut,
#     generations,
#     stats,
#     hof,
#     True
# )

# max, avg = logbook.select('max','avg')

# plt.plot(max, color='red')
# plt.plot(avg, color='green')
# plt.ylabel('max/avg fitness per generation')
# plt.xlabel('generation')
# plt.show()
