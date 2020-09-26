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
    SA.getSysInfo()

    # run SA to solve the problem
    SA.solve(myProblem)