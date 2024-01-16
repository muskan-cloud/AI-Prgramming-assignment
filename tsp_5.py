import random
import numpy as np

class AntColonyTSP:
    def __init__(self, num_ants, num_cities, distances, evaporation_rate=0.5, alpha=1, beta=2, iterations=100):
        self.num_ants = num_ants
        self.num_cities = num_cities
        self.distances = distances
        self.evaporation_rate = evaporation_rate
        self.alpha = alpha
        self.beta = beta
        self.iterations = iterations
        self.pheromone_levels = np.ones((num_cities, num_cities))

    def select_next_city(self, ant, visited):
        pheromone = self.pheromone_levels[ant.current_city]
        not_visited = np.delete(np.arange(self.num_cities), visited)
        probabilities = (pheromone[not_visited] ** self.alpha) * ((1 / self.distances[ant.current_city, not_visited]) ** self.beta)
        probabilities /= np.sum(probabilities)
        next_city = np.random.choice(not_visited, p=probabilities)
        return next_city

    def update_pheromones(self, ants):
        self.pheromone_levels *= self.evaporation_rate
        for ant in ants:
            for i in range(self.num_cities - 1):
                self.pheromone_levels[ant.tour[i], ant.tour[i + 1]] += 1 / self.distances[ant.tour[i], ant.tour[i + 1]]
            self.pheromone_levels[ant.tour[-1], ant.tour[0]] += 1 / self.distances[ant.tour[-1], ant.tour[0]]

    def ant_colony_optimization(self):
        best_tour = None
        best_cost = float('inf')

        for _ in range(self.iterations):
            ants = [Ant(self.num_cities) for _ in range(self.num_ants)]
            for ant in ants:
                while not ant.complete_tour():
                    next_city = self.select_next_city(ant, ant.tour)
                    ant.move_to_city(next_city)

            for ant in ants:
                cost = sum(self.distances[ant.tour[i], ant.tour[i + 1]] for i in range(self.num_cities - 1))
                cost += self.distances[ant.tour[-1], ant.tour[0]]
                if cost < best_cost:
                    best_cost = cost
                    best_tour = ant.tour

            self.update_pheromones(ants)
        print(best_cost)
        return best_tour

class Ant:
    def __init__(self, num_cities):
        self.num_cities = num_cities
        self.tour = [random.randint(0, num_cities - 1)]
        self.current_city = self.tour[0]

    def move_to_city(self, city):
        self.tour.append(city)
        self.current_city = city

    def complete_tour(self):
        return len(self.tour) == self.num_cities

def read_input():
    mode = input().strip()
    n = int(input().strip())
    coordinates = [list(map(float, input().strip().split())) for _ in range(n)]
    distances = [[float(x) for x in input().strip().split()] for _ in range(n)]
    return mode, n, coordinates, distances


if __name__ == "__main__":
    mode, num_cities, coords, dist_matrix = read_input()

    if mode == 'EUCLIDEAN':
        ant_colony = AntColonyTSP(num_ants=10, num_cities=num_cities, distances=np.array(dist_matrix))
        best_tour = ant_colony.ant_colony_optimization()
        if best_tour:
            print(' '.join(map(str, best_tour)))
        else:
            print("No solution found.")
    elif mode == 'NON-EUCLIDEAN':
        ant_colony = AntColonyTSP(num_ants=10, num_cities=num_cities, distances=np.array(dist_matrix))
        best_tour = ant_colony.ant_colony_optimization()
        if best_tour:
            print(' '.join(map(str, best_tour)))
        else:
            print("No solution found.")
    else:
        print("Invalid mode")
