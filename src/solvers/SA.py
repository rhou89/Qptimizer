import numpy as np

from src.solvers.Solver import Solver
from src.problems.Problem import Problem

class SimulatedAnnealing(Solver):
    
    def __init__(self, Method = 'Sequential'):
        self.setlinearScheme()
        self.setflipMethod(Method)

    def setflipMethod(self, Method):
        if Method == 'Sequential':
            self.flipTrial = 'Sequential'
        elif Method == 'Radom':
            self.flipTrial = 'Radom'
        else:
            print('Set flip method failed, it can only be Sequential or Radom')
    
    def setAnnealingScheme(self, Scheme):
        self.beta_list = Scheme

    def setlinearScheme(self, beta_init=0, beta_max=5, beta_step=10000):
        self.setAnnealingScheme(np.linspace(beta_init,beta_max,beta_step))

    def solve(self, problem):
        print('='*40, 'Preprocessing', '='*40)
        num_spin = problem.num_spin
        edges = []
        for item in problem.edges:
            edges.append(list(item)+[problem.edges[item]])

        nn = [[] for _ in range(num_spin)]
        wg = [[] for _ in range(num_spin)]
        for item in edges:
            nn[item[0]].append(item[1])
            wg[item[0]].append(item[2])

            nn[item[1]].append(item[0])
            wg[item[1]].append(item[2])
        print('Done')

        print('='*40, 'Optimizing', '='*40)
        # start from a random state
        si = np.sign(np.random.random(num_spin)-0.5)
        # compute energy for initial state
        eg = sum(map(lambda x: -si[x[0]]*si[x[1]]*x[2], edges))

        # SA algorithm
        trialPool = list(range(num_spin))
        for beta in self.beta_list:

            # shuffle into random order if specified
            if self.flipTrial == 'Radom':
                np.random.shuffle(trialPool)

            for target in trialPool:
                eg_delta = si[nn[target]].dot(wg[target])*si[target]*2 # energy difference
                
                # Metropolis update
                if eg_delta<0 or np.random.random()<np.exp(-eg_delta*beta):
                    si[target] = -si[target]
                    eg += eg_delta
        
        print('Done')
        print(f'Solution found with energy {eg}')
        return si, eg