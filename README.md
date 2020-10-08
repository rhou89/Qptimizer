# The QBenchmark Project

This project aims to provide a *fair* benchmark result for a class of optimizers and solvers on different problems.

As the library of algorithms can be huge and the types of problems are versatile, we welcome all kinds of contributions from you.

Feel free to use any code or data here for your project and/or research.

## Benchmark methodology
For problems with known best solutions (planted problems), we use the following criteria to assess the performance of different algorithms:
- Time-to-solution (TTS): the runtime required to find the best solution (with a probability 99% if it is heuristic algorithm).

For problems without known best solutions, we use similar quantity time-to-target (TTT) to assess the performance. The target could be the best known answer or some estimates.

### Algorithms
#### Available now
- Monte Carlo methods (random walkers)
  - Simulated annealing
  - Parallel tempering

#### Under development
- Classical algorithms
  - Tabu search
- Machine learning and neural network
  - Hopfield recurrent neural network

### Problems
- Random tile planting Ising model on periodic 2D square lattice
- Max-SAT 2016 random test sets

## Usage
Please refer to the tutorial folder for tutorials and demo scripts.
