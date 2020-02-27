import sys
import random
import time
sys.path.insert(0, '../tools/aima')
from search import Problem, hill_climbing, simulated_annealing

t = {}

t[1] = 19
t[4] = 17


class Town:

    def __init__(self, id):
        self.neighbors = {}
        self.id = id
    
    def setNeighbor(self, id, distance):
        self.neighbors[id] = distance
    
    def getDistance(self, id):
        if(id == self.id):
            return 0
        return self.neighbors[id]

    def __str__(self):
        string = ''
        for key, value in self.neighbors.items():
            string += "Neighbor: " + str(key) + " Distance: " + str(value) + "\n"
        return "Town " + str(self.id) + "\n" + string

class World:

    def __init__(self, numberOfTowns):
        self.towns = {}
        for i in range(numberOfTowns):
            town = Town(i)
            self.towns[i] = town
        for i in range(numberOfTowns):
            for j in range(numberOfTowns):
                if(i == j):
                    continue
                dist = random.randint(1, 100)
                self.setDistance(i, j, dist)
        
        for key, value in self.towns.items():
            print("\n")
            print(value)
            print("\n")


    def setDistance(self, town1, town2, distance):
        self.towns[town1].setNeighbor(town2, distance)
        self.towns[town2].setNeighbor(town1, distance)

    def calculateDistance(self, town1, town2):
        return self.towns[town1].getDistance(town2)


class TSP(Problem):
    """
    State: x value for the sine function variant f(x)
    Move: a new x value delta steps from the current x (in both directions) 
    """
    
    def __init__(self, world, initial, maximum=30, delta=0.001):
        self.world = world
        self.delta = delta
        self.initial = initial
        
        
    def actions(self, state):
        result1 = state[:]
        result2 = state[:]
        self.shuffle(result1)
        self.shuffle(result2)
        print("Value1:")
        print(self.value(result1))
        print("Value2:")
        print(self.value(result2))
        return [result1, result2] 
    
    def result(self, stateIgnored, x):
        return x
    
    def value(self, path):
        totalDistance = 0

        for town in path:
            nextTown = (path.index(town) + 1)
            if(nextTown >= len(path)):
                break
            totalDistance += self.world.calculateDistance(town, nextTown)
        
        totalDistance += self.world.calculateDistance(path[0], path[-1])

        return -totalDistance
    
    def shuffle(self, path):
        print("Printing Shuffle")
        first = path[0]
        rest = path[1:]
        print("Start")
        print(rest)
        
        random.shuffle(rest)
        print("Shuffled")
        print(rest)
        result = []
        result.append(first)
        
        for town in rest:
            result.append(town)
        print("Result")
        print(result)
        return result

if __name__ == "__main__":
    towns = 10
    world = World(towns)
    path = []
    for i in range(towns):
        path.append(i)
    
    random.shuffle(path)
    print(path)
    tsp = TSP(world, path)
    print('Initial                      x: ' + str(tsp.initial)
          + '\t\tvalue: ' + str(tsp.value(path))
          )

    startHill = time.time()
    # Solve the problem using hill-climbing.
    hill_solution = hill_climbing(tsp)
    endHill = time.time()
    print('Hill-climbing solution       x: ' + str(hill_solution)
          + '\tvalue: ' + str(tsp.value(hill_solution))
          )
    print("Time taken was", round(endHill - startHill, 7))    