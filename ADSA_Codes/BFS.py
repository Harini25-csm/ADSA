from collections import deque

# Function to perform BFS
def bfs(graph, start):
    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            queue.extend(neighbor for neighbor in graph[node] if neighbor not in visited)

# Function to read the graph from user input
def read_graph():
    graph = {}
    num_nodes = int(input("Enter the number of nodes: "))

    for _ in range(num_nodes):
        node = input("Enter node: ")
        neighbors = input(f"Enter neighbors for node {node} (separate with space): ").split()
        graph[node] = neighbors

    return graph

# Main program
graph = read_graph()
start_node = input("Enter the starting node for BFS: ")
print(f"\nBreadth-First Search starting from node {start_node}:")
bfs(graph, start_node)
