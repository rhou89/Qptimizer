# A simple demo about how to use and customize the MCMC solvers to solve an Ising problem

import numpy as np

# user-defined libs
from src.solvers.SA import SimulatedAnnealing as SA
from src.solvers.PT import ParallelTempering as PT
from src.problems.Ising import Ising

if __name__ == '__main__':

    # The first step is to define your problem 
    myProblem = Ising() # Create a problem instance
    myProblem.import_IsingChook(10, 1) # Import an Ising problem from predefined library
    myProblem.get_info() # Print problem information to screen. This is not necessary if you just want to try the solver out.

    # An optional step here is to print system information to screen
    SA.getSysInfo()  # We record CPU and memory information for better benchmark

    # The last step is to create an instance of your solver
    mySA = SA() # SA solver as an example
    mySA.solve(myProblem) # Use predefined SA solver to solve the problem.

    # You may also custermize the solver
    mySA.setflipMethod('Radom') # The default setting is sequential flip
    # The default annealing scheme is linear, but you can use any scheme by inputting beta in time sequence
    mySA.setAnnealingScheme(reversed([5*0.99**ii for ii in range(10000)]))
    mySA.solve(myProblem)

    # The PT solver is similar to the SA solver
    myPT = PT()
    myPT.solve(myProblem)
