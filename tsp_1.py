import time

class Node:
    def __init__(self, level, path, bound):
        self.level = level
        self.path = path
        self.bound = bound

def create_graph(distances):
    return distances  # For non-Euclidean case, distances are the graph

def tsp_branch_and_bound(distances):
    num_cities = len(distances)
    min_tour = []
    min_cost = float('inf')

    graph = create_graph(distances)

    initial_node = Node(level=0, path=[0], bound=0)
    queue = [initial_node]

    while queue:
        current_node = queue.pop()

        if current_node.level == num_cities - 1:
            current_cost = sum(graph[current_node.path[i]][current_node.path[i + 1]]
                               for i in range(num_cities - 1))
            current_cost += graph[current_node.path[-1]][current_node.path[0]]

            if current_cost < min_cost:
                min_cost = current_cost
                min_tour = current_node.path[:] + [0]  # Returning back to the start

        else:
            for city in range(num_cities):
                if city not in current_node.path:
                    new_path = current_node.path + [city]

                    bound = current_node.bound
                    bound += graph[current_node.path[current_node.level]][city]
                    for i in range(current_node.level + 1, num_cities):
                        if i < len(new_path):
                            bound += min(graph[new_path[i]][j] for j in range(num_cities) if j != city)

                    if bound < min_cost:
                        new_node = Node(level=current_node.level + 1, path=new_path, bound=bound)
                        queue.append(new_node)

    return min_tour

def read_input():
    mode = input().strip()
    n = int(input().strip())
    coordinates = [list(map(float, input().strip().split())) for _ in range(n)]
    distances = [[float(x) for x in input().strip().split()] for _ in range(n)]
    return mode, n, coordinates, distances

def main():
    mode, num_cities, coords, dist_matrix = read_input()
    start_time = time.time()  # Record the start time
    if mode == 'EUCLIDEAN':
        tour = tsp_branch_and_bound(dist_matrix)
        print(' '.join(map(str, tour)))
    elif mode == 'NON-EUCLIDEAN':
        tour = tsp_branch_and_bound(dist_matrix)
        print(' '.join(map(str, tour)))
    else:
        print("Invalid mode")
    
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Elapsed Time: {elapsed_time} seconds")

if __name__ == "__main__":
    main()
