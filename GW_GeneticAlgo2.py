!pip install deap
class Guard:


    def __init__(self, hardConstraintPenalty):

        self.hardConstraintPenalty = hardConstraintPenalty

        # list of guards:
        self.guards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']


        self.shiftPreference = [[1, 0, 0], [1, 1, 0], [0, 0, 1], [0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 1, 1], [1, 1, 1]]

        self.shiftMin = [2, 2, 1]
        self.shiftMax = [3, 4, 2]

        # max shifts per week allowed for each guard
        self.maxShiftsPerWeek = 5

        # number of weeks we create a schedule for:
        self.weeks = 1

        # useful values:
        self.shiftPerDay = len(self.shiftMin)
        self.shiftsPerWeek = 7 * self.shiftPerDay

    def __len__(self):

        return len(self.guards) * self.shiftsPerWeek * self.weeks


    def getCost(self, schedule):

        guardShiftsDict = self.getGuardShifts(schedule)


        consecutiveShiftViolations = self.countConsecutiveShiftViolations(guardShiftsDict)
        shiftsPerWeekViolations = self.countShiftsPerWeekViolations(guardShiftsDict)[1]
        guardsPerShiftViolations = self.countGuardsPerShiftViolations(guardShiftsDict)[1]
        shiftPreferenceViolations = self.countShiftPreferenceViolations(guardShiftsDict)


        hardContstraintViolations = consecutiveShiftViolations + guardsPerShiftViolations + shiftsPerWeekViolations
        softContstraintViolations = shiftPreferenceViolations

        return self.hardConstraintPenalty * hardContstraintViolations + softContstraintViolations

    def getGuardShifts(self, schedule):

        shiftsPerGuard = self.__len__() // len(self.guards)
        guardShiftsDict = {}
        shiftIndex = 0

        for guard in self.guards:
            guardShiftsDict[guard] = schedule[shiftIndex:shiftIndex + shiftsPerGuard]
            shiftIndex += shiftsPerGuard

        return guardShiftsDict

    def countConsecutiveShiftViolations(self, guardShiftsDict):

        violations = 0
        # iterate over the shifts of each guard:
        for guardShifts in guardShiftsDict.values():
            # look for two cosecutive '1's:
            for shift1, shift2 in zip(guardShifts, guardShifts[1:]):
                if shift1 == 1 and shift2 == 1:
                    violations += 1
        return violations

    def countShiftsPerWeekViolations(self, guardShiftsDict):

        violations = 0
        weeklyShiftsList = []
        # iterate over the shifts of each guard:
        for guardShifts in guardShiftsDict.values():  # all shifts of a single guard
            # iterate over the shifts of each weeks:
            for i in range(0, self.weeks * self.shiftsPerWeek, self.shiftsPerWeek):
                # count all the '1's over the week:
                weeklyShifts = sum(guardShifts[i:i + self.shiftsPerWeek])
                weeklyShiftsList.append(weeklyShifts)
                if weeklyShifts > self.maxShiftsPerWeek:
                    violations += weeklyShifts - self.maxShiftsPerWeek

        return weeklyShiftsList, violations

    def countGuardsPerShiftViolations(self, guardShiftsDict):

        totalPerShiftList = [sum(shift) for shift in zip(*guardShiftsDict.values())]

        violations = 0
        # iterate over all shifts and count violations:
        for shiftIndex, numOfGuards in enumerate(totalPerShiftList):
            dailyShiftIndex = shiftIndex % self.shiftPerDay  # -> 0, 1, or 2 for the 3 shifts per day
            if (numOfGuards > self.shiftMax[dailyShiftIndex]):
                violations += numOfGuards - self.shiftMax[dailyShiftIndex]
            elif (numOfGuards < self.shiftMin[dailyShiftIndex]):
                violations += self.shiftMin[dailyShiftIndex] - numOfGuards

        return totalPerShiftList, violations

    def countShiftPreferenceViolations(self, guardShiftsDict):

        violations = 0
        for guardIndex, shiftPreference in enumerate(self.shiftPreference):
            # duplicate the shift-preference over the days of the period
            preference = shiftPreference * (self.shiftsPerWeek // self.shiftPerDay)
            # iterate over the shifts and compare to preferences:
            shifts = guardShiftsDict[self.guards[guardIndex]]
            for pref, shift in zip(preference, shifts):
                if pref == 0 and shift == 1:
                    violations += 1

        return violations

    def printScheduleInfo(self, schedule):

        guardShiftsDict = self.getGuardShifts(schedule)

        print("Schedule for each guard:")
        for guard in guardShiftsDict:  # all shifts of a single guard
            print(guard, ":", guardShiftsDict[guard])

        print("consecutive shift violations = ", self.countConsecutiveShiftViolations(guardShiftsDict))
        print()

        weeklyShiftsList, violations = self.countShiftsPerWeekViolations(guardShiftsDict)
        print("weekly Shifts = ", weeklyShiftsList)
        print("Shifts Per Week Violations = ", violations)
        print()

        totalPerShiftList, violations = self.countGuardsPerShiftViolations(guardShiftsDict)
        print("Guards Per Shift = ", totalPerShiftList)
        print("Guards Per Shift Violations = ", violations)
        print()

        shiftPreferenceViolations = self.countShiftPreferenceViolations(guardShiftsDict)
        print("Shift Preference Violations = ", shiftPreferenceViolations)
        print()

        ##### GA #################################

guard = Guard(10)

def eaSimpleWithElitism(population, toolbox, cxpb, mutpb, ngen, stats=None,
             halloffame=None, verbose=__debug__):

    logbook = tools.Logbook()
    logbook.header = ['gen', 'nevals'] + (stats.fields if stats else [])

    # Evaluate the individuals with an invalid fitness
    invalid_ind = [ind for ind in population if not ind.fitness.valid]
    fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
    for ind, fit in zip(invalid_ind, fitnesses):
        ind.fitness.values = fit

    if halloffame is None:
        raise ValueError("halloffame parameter must not be empty!")

    halloffame.update(population)
    hof_size = len(halloffame.items) if halloffame.items else 0

    record = stats.compile(population) if stats else {}
    logbook.record(gen=0, nevals=len(invalid_ind), **record)
    if verbose:
        print(logbook.stream)

    # Begin the generational process
    for gen in range(1, ngen + 1):

        # Select the next generation individuals
        offspring = toolbox.select(population, len(population) - hof_size)

        # Vary the pool of individuals
        offspring = algorithms.varAnd(offspring, toolbox, cxpb, mutpb)

        # Evaluate the individuals with an invalid fitness
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = toolbox.map(toolbox.evaluate, invalid_ind)
        for ind, fit in zip(invalid_ind, fitnesses):
            ind.fitness.values = fit

        # add the best back to population:
        offspring.extend(halloffame.items)

        # Update the hall of fame with the generated individuals
        halloffame.update(offspring)

        # Replace the current population by the offspring
        population[:] = offspring

        # Append the current generation statistics to the logbook
        record = stats.compile(population) if stats else {}
        logbook.record(gen=gen, nevals=len(invalid_ind), **record)
        if verbose:
            print(logbook.stream)

    return population, logbook




import numpy as np
import matplotlib.pyplot as plt
import random
from deap import base, tools, creator, algorithms

popSize = 300
generations = 1000
chromSize = 7 * 3 * 8
pCX = 0.7
pMut = 0.2

random.seed(42)

## Set up toolbox

toolbox = base.Toolbox()
toolbox.register('binary', random.randint,0,1)


creator.create('fitnessMin', base.Fitness,weights=(-1.0,))
creator.create('Individual',list,
               fitness = creator.fitnessMin)
toolbox.register('createIndividual',tools.initRepeat,
                creator.Individual, toolbox.binary,
                len(guard))
toolbox.register('createPop',tools.initRepeat, list,
                 toolbox.createIndividual)


def fitnessFunction(individual):
   return guard.getCost(individual),

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
stats.register('min', np.min)
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

min, avg = logbook.select('min','avg')

plt.plot(min, color='red')
plt.plot(avg, color='green')
plt.ylabel('min/avg fitness per generation')
plt.xlabel('generation')
plt.show()

best = hof[0]

guard.printScheduleInfo(best)
