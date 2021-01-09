# A simple demo on defining and customizing Ising problems

import numpy as np

# user-defined libs
from src.problems.Ising import Ising

if __name__ == '__main__':

    myProblem = Ising() # Create an Ising problem instance
    # add edges to the problem [node0, node1, ... , weight]
    # onsite bias
    myProblem.addEdge([0, 0.5])
    # 2nd order coupling
    myProblem.addEdge([1, 5, 9])
    myProblem.addEdge([0, 1, 5])
    myProblem.addEdge([2, 3, -1])
    myProblem.addEdge([5, 3, 1.0])
    myProblem.printProblem()

    # order of nodes does not matter
    # adding an existing edge will change the weight
    myProblem.addEdge([4, 1, -1/3])
    myProblem.addEdge([3, 5, 1.5])
    myProblem.printProblem()
    myProblem.get_info()

    # you may also import default test sample problem
    # CAUTION: this will automatically clear any existing problem in myProblem
    myProblemFile = myProblem.import_IsingChook(problem_size=4, instance=1)
    myProblem.printProblem()
    myProblem.get_info()
