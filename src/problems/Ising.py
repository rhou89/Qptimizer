# -*- coding: utf-8 -*-

'''
The Ising class is a derived class from problem.
One instance of the Ising class corresponds to a given Ising problem.
The class has the following members:

Methods:
    __init__():
    clear():
    import_IsingChook():
    get_info():

Variables:
    problem_type

    num_spin: the number of spins in this Ising problem
    edges: store all the edges in the Ising problem
    best_sol: store the best known solution to the problem
    best_config: store the corresponding spin configuration of the best known solution
'''

import os

from src.problems.Problem import Problem

class Ising(Problem):
    def __init__(self):
        self.problem_type = 'Ising'
        self.clear()

    # Method: clear current problem
    def clear(self):
        self.edges = []
        self.num_spin = 0
        self.best_sol = None
        self.best_config = None

    def addEdge(self, x1, x2, weight):
        self.edges.append([x1, x2, weight])

    def chookSamplePath(self, problem_size, instance):
        # file to be read
        targetFolder = f'tile_planting_2D_L_{problem_size}_p1_0.2_p2_0.5_p3_0.1'
        targetFile = f'{targetFolder}_inst_{instance}.txt'
        problemPath = os.path.join('data', 'Ising_chook', targetFolder, targetFile)
        energyPath = os.path.join('data', 'Ising_chook', targetFolder, 'gs_energies.txt')
        if os.path.isfile(problemPath) and os.path.isfile(energyPath):
            return problemPath, energyPath

        print('The given chook data does not exist, please check again.')
        return None, None

    # import chook Ising problem
    def import_IsingChook(self, problem_size=4, instance=1):
        # clear any previous problem
        self.clear()

        # define problem files
        targetFolder = f'tile_planting_2D_L_{problem_size}_p1_0.2_p2_0.5_p3_0.1'
        targetFile = f'{targetFolder}_inst_{instance}.txt'

        # read from file
        with open(f'data/Ising_chook/{targetFolder}/{targetFile}', 'r') as f:
            line = f.readline().split()
            while len(line)>1:
                self.edges.append(list(map(int, line)))
                line = f.readline().split()

        # other updates
        self.num_spin = problem_size**2
        with open(f'data/Ising_chook/{targetFolder}/gs_energies.txt', 'r') as f:
            line = f.readline().split()
            while len(line)>1:
                if line[0] == targetFile:
                    self.best_sol = int(line[1])
                    break
                line = f.readline().split()

    # print problem information
    def get_info(self):
        print('='*40, 'Problem Info', '='*40)
        print(f'The problem is a/an {self.problem_type} type problem')
        print(f'Number of variables: {self.num_spin}')
        print(f'Number of coupling: {len(self.edges)}')
        if self.best_sol != float('inf'):
            print(f'This is planted problem with known best solution: {self.best_sol}')