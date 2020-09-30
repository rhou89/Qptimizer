import numpy as np

# user-defined libs
from src.SA import SimulatedAnnealing as SA
from src.problem import problem

if __name__ == '__main__':

    # create a problem instance
    myProblem = problem()
    # import an Ising problem
    myProblem.import_IsingChook(10, 1)
    # print problem information to screen
    myProblem.get_info()

    # print system information to screen
    # we record CPU and memory information for better benchmark results
    SA.getSysInfo()

    # create an instance for SA solver
    mySA = SA()
    # customize your solver
    # the default setting is sequential flip
    mySA.setflipMethod('Radom')
    # the default annealing scheme is linear, but you can use any scheme by inputting beta in time sequence
    beta_seq = [5*0.99**ii for ii in range(2000)]
    mySA.setAnnealingScheme(beta_seq.reverse())
    # run the solver to solve the problem
    mySA.solve(myProblem)