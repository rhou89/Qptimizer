import numpy as np

# user-defined libs
from src.solver import solver as sr

if __name__ == '__main__':
    # sr.getSysInfo()

    # gs = -255 in this case
    problem = []
    with open('data/Ising_chook/tile_planting_2D_L_12_p1_0.2_p2_0.5_p3_0.1/tile_planting_2D_L_12_p1_0.2_p2_0.5_p3_0.1_inst_1.txt', 'r') as f:
        line = f.readline().split()
        while len(line)>1:
            problem.append(list(map(int, line)))
            line = f.readline().split()
    
    num_spin = 12**2
    nn = [[] for _ in range(num_spin)]
    wg = [[] for _ in range(num_spin)]
    for item in problem:
        nn[item[0]].append(item[1])
        wg[item[0]].append(item[2])

        nn[item[1]].append(item[0])
        wg[item[1]].append(item[2])

    # start from a random state
    si = np.sign(np.random.random(num_spin)-0.5)
    # compute energy for initial state
    eg = sum(map(lambda x: -si[x[0]]*si[x[1]]*x[2], problem))
    # use reciprocal temperature beta here
    # linear annealing scheme in this example
    beta_init = 0
    beta_max = 5
    beta_step = 0.005

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

    print(eg)