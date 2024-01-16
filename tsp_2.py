import random
import time

class GeneticAlgorithmTSP:
    def __init__(self, num_cities, distances):
        self.num_cities = num_cities
        self.distances = distances
        self.population_size = 50
        self.mutation_rate = 0.02
        self.elite_size = 5
        self.max_generations = 1000

    def create_individual(self):
        return random.sample(range(self.num_cities), self.num_cities)

    def initial_population(self):
        return [self.create_individual() for _ in range(self.population_size)]

    def calculate_fitness(self, individual):
        total_distance = 0
        for i in range(self.num_cities - 1):
            total_distance += self.distances[individual[i]][individual[i + 1]]
        total_distance += self.distances[individual[-1]][individual[0]]
        return total_distance

    def rank_population(self, population):
        return sorted(population, key=lambda x: self.calculate_fitness(x))

    def selection(self, ranked_population):
        return ranked_population[:self.elite_size]

    def breed(self, parent1, parent2):
        start = random.randint(0, self.num_cities - 1)
        end = random.randint(0, self.num_cities - 1)

        if start > end:
            start, end = end, start

        child = [None] * self.num_cities
        for i in range(start, end):
            child[i] = parent1[i]

        remaining = [item for item in parent2 if item not in child]

        for i in range(self.num_cities):
            if child[i] is None:
                child[i] = remaining.pop(0)

        return child

    def crossover(self, elite):
        children = []
        while len(children) < self.population_size - self.elite_size:
            parent1 = random.choice(elite)
            parent2 = random.choice(elite)
            child = self.breed(parent1, parent2)
            children.append(child)
        return children

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            idx1, idx2 = random.sample(range(self.num_cities), 2)
            individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
        return individual

    def next_generation(self, current_gen):
        elite = self.selection(self.rank_population(current_gen))
        children = self.crossover(elite)
        next_gen = elite + children

        next_gen_mutated = [self.mutate(individual) for individual in next_gen]

        return next_gen_mutated

    def genetic_algorithm(self):
        start_time = time.time()

        population = self.initial_population()
        for generation in range(self.max_generations):
            population = self.next_generation(population)

            best_individual = self.rank_population(population)[0]
            best_fitness = self.calculate_fitness(best_individual)

            if time.time() - start_time > 300:  # Time limit: 300 seconds
                break

        return best_individual, best_fitness


def read_input():
    mode = input().strip()
    n = int(input().strip())
    coordinates = [list(map(float, input().strip().split())) for _ in range(n)]
    distances = [[float(x) for x in input().strip().split()] for _ in range(n)]
    return mode, n, coordinates, distances

def main():
    mode, num_cities, coords, dist_matrix = read_input()

    if mode == 'EUCLIDEAN':
        ga_tsp = GeneticAlgorithmTSP(num_cities, dist_matrix)
        best_tour, best_cost = ga_tsp.genetic_algorithm()
        print(' '.join(map(str, best_tour)))
        print(best_cost)
    elif mode == 'NON-EUCLIDEAN':
        ga_tsp = GeneticAlgorithmTSP(num_cities, dist_matrix)
        best_tour, best_cost = ga_tsp.genetic_algorithm()
        print(' '.join(map(str, best_tour)))
        print(best_cost)
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()
