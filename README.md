# The QBenchmark Project

The **QBenchmark** project aims to provide a *fair* benchmark result for a class of optimizers on different problems.

As the library of algorithms can be huge and the types of problems are versatile, we welcome all kinds of contributions from you.

Feel free to use any code or data here for your project and/or research.

<!--
## Benchmark methodology
For problems with known best solutions (planted problems), we use the following criteria to assess the performance of different algorithms:
- Time-to-solution (TTS): the runtime required to find the best solution (with a probability 99% if it is heuristic algorithm).

For problems without known best solutions, we use similar quantity time-to-target (TTT) to assess the performance. The target could be the best known answer or some estimates.

All the algorithm are benchmarked with the Python code we developed in the src folder, which makes sure that we are comparing "apples" to "apples".

As there is "no free lunch", the benchmark results vary on different problems. The objective is to cover as many different problems as possible.

-->

# The Qptimizer Project

The **Qptimizer** project is part of the **QBenchmark** project that provides versatile optimizers with user-configurable search strategy. We also provide relevant references and tutorials about how to configure and reuse the optimizers to solve your own problems.

### Algorithms
You are welcome to fork and use the source codes since all the algorithms have been published in some journals and/or preprints.

#### Available now
- Monte Carlo methods (random walkers)
  - Simulated annealing
  - Parallel tempering

#### Under development
- Classical algorithms
  - Tabu search
  - Evolutionary algorithm
  - Ant colony optimization
 
- Machine learning and neural network
  - Hopfield recurrent neural network
  
- Monte Carlo methods
  - Population annealing
  
### Problems
The currently available test sets are listed on the following:

- Random tile planting Ising model on periodic 2D square lattice
- Max-SAT 2016 random test sets

## Usage
Please refer to the tutorial folder for tutorials and demo scripts.
