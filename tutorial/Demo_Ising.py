# A simple demo on defining and customizing Ising problems

import numpy as np

# user-defined libs
from src.problems.Ising import Ising

if __name__ == '__main__':

    myProblem = Ising() # Create an Ising problem instance
    myProblem.addEdge(1, 5, 9)
    
    myProblemFile = myProblem.chookSamplePath(10, 1) # Import an Ising problem from predefined library
    
    #myProblem.get_info() # Print problem information to screen. This is not necessary if you just want to try the solver out.
