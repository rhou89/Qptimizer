import numpy as np

from src.solver import solver
from src.problem import problem
class SimulatedAnnealing(solver):
    def __init__(self):
        pass

    @staticmethod
    def solve(problem, annealingScheme = 'Linear'):

        print('='*40, 'Preprocessing', '='*40)
        num_spin = problem.num_spin
        edges = problem.edges

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
        # use reciprocal temperature beta here
        # linear annealing scheme in this example
        beta_init = 0
        beta_max = 5
        beta_step = 0.001

        # SA algorithm
        beta = beta_init
        while beta < beta_max:
            # sequential flip in this example
            for target in range(num_spin):
                eg_delta = si[nn[target]].dot(wg[target])*si[target]*2 # energy difference
                
                # Metropolis update
                if eg_delta<0 or np.random.random()<np.exp(-eg_delta*beta):
                    si[target] = -si[target]
                    eg += eg_delta
            
            # cooling down
            beta += beta_step
        
        print('Done!')
        print(f'Solution found with energy {eg}')
        return si, eg