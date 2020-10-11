import numpy as np

from src.solver import solver
from src.Problem import Problem

class Hopfield(solver):

    def __init__(self):
        # There are various models of HNN and we only support HTNN now
        self.method = 'HTNN'

    def solve(self, problem: Problem):
        # Call seed() to ensure random instace in parallel computing
        np.random.seed()

        if self.method == 'HTNN':
            self.HTNN(problem)

    def HTNN(self, problem: Problem):
        num_spin = problem.num_spin
        Ising_H = np.zeros([num_spin, num_spin])
        for edge in problem.edges:
            Ising_H[edge[0],edge[1]] = edge[2]
            Ising_H[edge[1],edge[0]] = edge[2]

        si = (np.random.rand(num_spin)-0.5)*2 # Initial random configuration

        # algorithm parameters
        beta = 10 # beta is a controlling parameter
        beta_min = 0.001 # terminating value
        update_th = 0.001 # control when beta is updated
        update_coff = 0.8
        noise_rate = 0.8

        dt = 0.5 # time step for Euler integration
        max_step = 50000 # terminating step
        # stop_precision = 1e-2

        # solving ODE
        for _ in range(max_step):
            dsi = -si + np.dot(Ising_H, np.tanh(si/beta))
            if np.abs(dsi).sum()<update_th:
                beta *= update_coff
            
            dsi += np.random.normal(0, noise_rate, num_spin)
            si += dsi*dt

            noise_rate = 0.99*noise_rate
            if beta < beta_min:
                break

        si = np.sign(np.tanh(si/beta))
        eg = -si.dot(Ising_H.dot(si))/2
        return si, eg
