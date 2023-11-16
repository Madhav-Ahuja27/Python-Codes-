# import numpy as np
# import matplotlib.pyplot as plt
# import random
# from deap import base,tools,creator,algorithms
# popSize=100
# gens=100
# p_c=0.9
# p_m=0.1
# random.seed(42)
# chromSize=7*3*8

# #toolbox
# toolbox=base.Toolbox()
# toolbox.register("binary",random.randint,0,1)
# creator.create=('FitnessMin',base.Fitness,
#                 weights=(-1.0,))
# creator.create('Indivisual',list,
#                fitness=creator.FitnessMin)
# toolbox.register('createIndivisual',tools.initRepeat,creator.Indivisual,toolbox.binary,len(pass))
# toolbox.register('createPop',tools.initRepeat,list,
#                  toolbox.createIndivisual)

# def fitnessFunction(indivisual):
#   return pass

# #operators
# toolbox.register('evaluate',fitnessFunction)
# toolbox.register('select',selTournament,tournsize=3)
# toolbox.register('crossover',tools.cxUniform,indpb=0.3)
# toolbox.register('mutation',tools.mutShuffleIndexes,
#                  indpb=1/chromSize)
# startingPop=toolbox.createPop(popSize)
# stats=tools.Statistics(lambda ind:ind.fitness.values)
# stats.register('min',np.min)
# stats=register('avg',np.mean)
# hof=tools.HallOfFame(5)
# finalPop,logbook=eaSimpleWithElitism(pass)
# min,avg=logbook.select('min','avg')

                                    #GLOBAL WEEK DAY 4
