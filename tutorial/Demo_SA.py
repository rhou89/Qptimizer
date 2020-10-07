# A simple demo about how to use and customize the SA solver to solve an Ising problem

import numpy as np

# user-defined libs
from src.SA import SimulatedAnnealing as SA
from src.problem import problem

if __name__ == '__main__':

    # The first step is to define your problem 
    myProblem = problem() # Create a problem instance
    myProblem.import_IsingChook(10, 1) # Import an Ising problem from predefined library
    myProblem.get_info() # Print problem information to screen. This is not necessary if you just want to try the solver out.

    # An optional step here is to print some system information to screen
    SA.getSysInfo()  # We record CPU and memory information for better benchmark

    # The last step is to create an instance of your solver
    mySA = SA() # SA solver as an example
    mySA.solve(myProblem) # Use predefined SA solver to solve the problem.

    # You may also custermize the solver
    mySA.setflipMethod('Radom') # The default setting is sequential flip
    # The default annealing scheme is linear, but you can use any scheme by inputting beta in time sequence
    beta_seq = [5*0.99**ii for ii in range(10000)]
    beta_seq.reverse()
    mySA.setAnnealingScheme(beta_seq)
    mySA.solve(myProblem)