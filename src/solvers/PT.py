import numpy as np

from src.solvers.Solver import Solver
from src.problems.Problem import Problem

class ParallelTempering(Solver):

    def __init__(self):
        pass

    def solve(self, problem):
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

        num_swps = 100 # number of Monte Carlo steps
        num_rep = 5 # number of replica
        beta = [0.01, 0.05, 0.25, 1, 5] # reverse temp for each replica

        # start from a random state
        si = [np.sign(np.random.randn(num_spin)) for _ in range(num_rep)]
        # compute energy for initial state
        eg = [sum(map(lambda x: -ss[x[0]]*ss[x[1]]*x[2], edges)) for ss in si]

        ans_eg = float('inf')
        ans_si = []

        for _ in range(num_swps):

            # Metropolis updates for each replica
            for _ in range(10):
                for ii in range(num_rep):
                    for flip in range(num_spin):
                        eg_delta = np.dot(si[ii][nn[flip]],wg[flip])*si[ii][flip]*2
                        
                        if (eg_delta<0) or (np.random.random()<np.exp(-eg_delta*beta[ii])):
                            si[ii][flip] = -si[ii][flip]
                            eg[ii] += eg_delta
            
            # swap replica at different/adjacent temperature
            for ii in range(num_rep-1):
                jj = ii+1 # or for jj in range(num_rep)
                chg_p = min(1, np.exp((eg[ii]-eg[jj])*(beta[ii]-beta[jj])))
                if np.random.random()<chg_p:
                    si[ii], si[jj] = si[jj], si[ii]
                    eg[ii], eg[jj] = eg[jj], eg[ii]

            for ii in range(num_rep):
                if eg[ii] < ans_eg:
                    ans_eg = eg[ii]
                    ans_si = si[ii]
            
        print('Done')
        print(f'Solution found with energy {ans_eg}')

        return ans_eg, ans_si