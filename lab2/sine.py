"""
This module implements local search on a simple sine function variant.
The function is a linear function  with a single, discontinuous max value
(see the sine function variant in graphs.py).

@author: kvlinden
@version 6feb2013
"""
from search import Problem, hill_climbing, simulated_annealing, \
    exp_schedule, genetic_search
from random import randrange
import math
import time


class Sine(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, initial, maximum=30, delta=0.001):
        self.initial = initial
        self.delta = delta
        
    def actions(self, state):
        return [state + self.delta, state - self.delta]
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, x):
        if(randrange(5) == 0):
            return self.initial
        result = math.fabs(x * math.sin(x) )
        if(result > maximum): 
            return maximum
        return result
        


if __name__ == '__main__':

    # Formulate a problem with a 2D hill function and a single maximum value.
    maximum = 30
    initial = randrange(0, maximum)
    p = Sine(initial, maximum, delta=5.0)
    print('Initial                      x: ' + str(p.initial)
          + '\t\tvalue: ' + str(p.value(initial))
          )

    startHill = time.time()
    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(p)
    endHill = time.time()
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(p.value(hill_solution))
          )
    print("Time taken was", round(endHill - startHill, 7))
    # Solve the problem using simulated annealing.
    startAnneal = time.time()
    annealing_solution = simulated_annealing(
        p,
        exp_schedule(k=20, lam=0.005, limit=1000)
    )
    endAnneal = time.time()
    print('Simulated annealing solution x: ' + str(annealing_solution)
          + '\tvalue: ' + str(p.value(annealing_solution))
          )
    print("Time taken was", round(endAnneal - startAnneal, 7))