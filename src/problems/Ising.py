# -*- coding: utf-8 -*-

'''
The Ising class is a derived class from problem. One instance of the Ising class realizes a given Ising problem. We have made the following assumption that the spin variables are denoted from 0 to any positive integer. The Ising problem should form an undirected graph.

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
import sys

from src.problems.Problem import Problem

class Ising(Problem):
    def __init__(self):
        self.problem_type = 'Ising'
        self.clear()
    
    # reset the best known solution
    def clearBestSol(self):
        self.best_sol = None
        self.best_config = None

    # reset all problem-specific properties
    def clear(self):
        self.edges = {}
        self.num_spin = 0
        self.clearBestSol()
    
    # add a new edge into the problem
    def addEdge(self, edge):
        # format input
        weight = self.checkNum(edge[-1])
        nodes = sorted(self.checkAllInt(edge[:-1]))

        # check input validity
        if len(nodes) < 1:
            sys.exit('To add an edge, a list of at least two elements is required.')
        if nodes[0] < 0:
            sys.exit('The nodes must be labelled from 0.')
        
        # add or update weight and number of spins
        self.edges[tuple(nodes)] = weight
        self.num_spin = max(self.num_spin, nodes[-1])

        # Once the problem is modified, the best known solution becomes invalid
        self.clearBestSol()
    
    # print the edge and its weight
    def printProblem(self):
        self.display('Problem Config')
        for edge in self.edges:
            print(edge, ':',  self.edges[edge])
    
    # get the path to a specific chook sample file
    def chookSamplePath(self, problem_size, instance):
        # file to be read
        targetFolder = f'tile_planting_2D_L_{problem_size}_p1_0.2_p2_0.5_p3_0.1'
        targetFile = f'{targetFolder}_inst_{instance}.txt'
        problemPath = os.path.join('data', 'Ising_chook', targetFolder, targetFile)
        energyPath = os.path.join('data', 'Ising_chook', targetFolder, 'gs_energies.txt')
        if os.path.isfile(problemPath) and os.path.isfile(energyPath):
            return problemPath, energyPath

        sys.exit('Can\'t find the problem data.')

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
                self.addEdge(list(map(int, line)))
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
        self.display('Problem Info')
        print(f'The problem is a/an {self.problem_type} type problem')
        print(f'Number of variables: {self.num_spin}')
        print(f'Number of coupling: {len(self.edges)}')
        if self.best_sol != None:
            print(f'This is planted problem with known best solution: {self.best_sol}')