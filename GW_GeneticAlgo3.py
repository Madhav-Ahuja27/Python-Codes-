import matplotlib.pyplot as plt
import numpy as np
from deap import base, creator, tools, algorithms
import multiprocessing
import random


class ACME:

    def __init__(self):
        self.total_violations = []
        self.cooldown = 10
        self.job_time = 20
        self.component_prod_times = [20, 40, 60, 20]
        self.machines = ['Alpha', 'Beta', 'Gamma', 'Delta', 'Eplison']
        self.components = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
        self.reconfig_time = [
            # A  B C  D E
            [0, 10, 15, 5, 7, 2, 8 , 30, 1000], #A
            [10, 0, 6, 12, 7, 4, 22, 90, 60], #B
            [15, 6, 0, 33, 40, 1000, 8, 10, 20], #C
            [5, 12, 33, 0, 70, 60, 5, 45, 24], #D
            [7, 7, 40, 70, 0, 35, 20, 10, 11], #E
            [2, 4, 1000, 60, 35, 0, 8, 1000, 8], #F
            [8, 22, 8, 5, 20, 8, 0, 17, 55], #G
            [30, 90, 10, 45, 10, 1000, 17, 0, 4], #H
            [1000, 60, 20, 25, 11, 8, 55, 4, 0], #I
        ]
        self.job_slots = 3 * 24

    def __len__(self):
        return len(self.machines) * self.job_slots


    def fitness(self, solution):
        minimum_components = 25
        violations = 0
        time = self.calc_reconfig_time(solution)


        for i in range(0,9):
            count = minimum_components - solution.count(i)
            if count>0:
                violations += count

        time += (violations * 1000)

        return time

    def calc_reconfig_time(self, solution):

        time = 0

        pairs = list(zip(solution, solution[1:]))

        for pair in pairs:
            time += self.reconfig_time[pair[0]][pair[1]]



        return time

    def print_schedule_details(self, solution):
        machineNo=0
        machines = []
        reconfig_times = []
        # split into machines
        lenth = 72
        current = 0
        next = lenth

        for i in range(len(self.machines)):
            machines.append(solution[current:next])
            current = next
            next +=lenth

        for machine in machines:
            machineNo+=1
            machine_list = []
            for job in machine:
                machine_list.append(self.components[job])
            print(f"job list machine {machineNo}: {machine_list}")
            time = 0

            pairs = list(zip(machine, machine[1:]))

            for pair in pairs:
                time += self.reconfig_time[pair[0]][pair[1]]
                reconfig_times.append(time)

            print(f"machine {machineNo} config time: {time}")




####################### elitism function ###############

def eaWithElitism(population, toolbox, cxpb, mutpb, ngen, stats=None,
                   halloffame=None, verbose=__debug__):
    """This algorithm is similar to DE"""
