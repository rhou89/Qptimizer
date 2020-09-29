# The QBenchmark Project

This project aims to provide a *fair* benchmark result for a class of optimizers and solvers on different problems.

As the library of algorithms can be huge and the types of problems are versatile, we welcome all kinds of contributions from you.

## Benchmark methodology
For problems with known best solutions (planted problems), we use two criteria to assess the performance of different algorithms:
- Time-to-solution (TTS): the runtime required to find the best solution with a probability 99%.

For problems without known best solutions, we compare the average runtime and the solution quality.

## Algorithms under test
- Classical algorithms
  - Tabu search
- Machine learning and neural network
  - Hopfield recurrent neural network
- Monte Carlo methods (random walkers)
  - Simulated annealing
  - Parallel tempering

## Test sets
- Random tile planting Ising model on periodic 2D square lattice
- Max-SAT 2016 random test sets
