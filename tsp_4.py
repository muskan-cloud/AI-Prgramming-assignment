class BranchAndBoundTSP:
    def __init__(self, num_cities, distances):
        self.num_cities = num_cities
        self.distances = distances
        self.best_tour = None
        self.best_cost = [float('inf')]

    def branch_and_bound(self):
        def dfs(node, visited, cost):
            if len(visited) == self.num_cities:
                if cost + self.distances[node][0] < self.best_cost[0]:
                    self.best_cost[0] = cost + self.distances[node][0]
                    self.best_tour = visited + [0]
                return

            for city in range(self.num_cities):
                if city not in visited and self.distances[node][city] != 0:
                    if cost + self.distances[node][city] < self.best_cost[0]:
                        dfs(city, visited + [city], cost + self.distances[node][city])

        dfs(0, [0], 0)
        return self.best_tour

def read_input():
    mode = input().strip()
    n = int(input().strip())
    coordinates = [list(map(float, input().strip().split())) for _ in range(n)]
    distances = [[float(x) for x in input().strip().split()] for _ in range(n)]
    return mode, n, coordinates, distances

def main():
    mode, num_cities, coords, dist_matrix = read_input()

    if mode == 'EUCLIDEAN':
        bnb_tsp = BranchAndBoundTSP(num_cities, dist_matrix)
        best_tour = bnb_tsp.branch_and_bound()
        if best_tour:
            print(' '.join(map(str, best_tour)))
        else:
            print("No solution found.")
    elif mode == 'NON-EUCLIDEAN':
        bnb_tsp = BranchAndBoundTSP(num_cities, dist_matrix)
        best_tour = bnb_tsp.branch_and_bound()
        if best_tour:
            print(' '.join(map(str, best_tour)))
        else:
            print("No solution found.")
    else:
        print("Invalid mode")

if __name__ == "__main__":
    main()
