# A simple demo about how to use and customize the HNN solvers to solve an Ising problem

import numpy as np

# user-defined libs
from src.solvers.Hopfield import Hopfield as HNN
from src.problems.Ising import Ising

if __name__ == '__main__':

    # Define problem and import an instance
    myProblem = Ising()
    myProblem.import_IsingChook(6, 1) 
    myProblem.get_info()

    # Use HTNN to solve the problem
    myHNN = HNN()
    _, ans = myHNN.solve(myProblem)
    print("Minimum found:", ans)
