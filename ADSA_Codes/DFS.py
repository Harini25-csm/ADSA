# Function to perform DFS
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    print(start, end=" ")
    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

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
start_node = input("Enter the starting node for DFS: ")
print(f"\nDepth-First Search starting from node {start_node}:")
dfs(graph, start_node)
