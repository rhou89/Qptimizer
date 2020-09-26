# we support only Ising problem right now

class problem:
    def __init__(self):
        self.problem_type = 'Ising'
        self.clear()

    # import chook Ising problem
    def import_IsingChook(self, problem_size=4, instance=1):
        # clear any previous problem
        self.clear()

        # file to be read
        targetFolder = f'tile_planting_2D_L_{problem_size}_p1_0.2_p2_0.5_p3_0.1'
        targetFile = f'{targetFolder}_inst_{instance}.txt'

        # read from file
        with open(f'data/Ising_chook/{targetFolder}/{targetFile}', 'r') as f:
            line = f.readline().split()
            while len(line)>1:
                self.edges.append(list(map(int, line)))
                line = f.readline().split()

        # other updates
        self.num_spin = problem_size**2
        with open(f'data/Ising_chook/{targetFolder}/gs_energies.txt', 'r') as f:
            line = f.readline().split()
            while len(line)>1:
                if line[0] == targetFile:
                    self.best_sol = int(line[1])
                    break
                line = f.readline().split()


    # print problem information
    def get_info(self):
        print('='*40, 'Problem Info', '='*40)
        print(f'The problem is a/an {self.problem_type} type problem')
        print(f'Number of variables: {self.num_spin}')
        print(f'Number of coupling: {len(self.edges)}')
        if self.best_sol != float('inf'):
            print(f'This is planted problem with known best solution: {self.best_sol}')
    
    # method: clear current problem
    def clear(self):
        self.edges = []
        self.num_spin = 0
        self.best_sol = float('inf')