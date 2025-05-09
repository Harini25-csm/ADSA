def bellman_ford(vertices, edges, source):
    # Initialize distances and predecessors
    dist = [float('inf')] * vertices
    dist[source] = 0
    predecessor = [-1] * vertices

    print(f"Initial distances: {dist}")

    # Relax edges (V - 1 times)
    for i in range(vertices - 1):
        print(f"\nIteration {i + 1}:")
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                predecessor[v] = u
        print(f"Distances: {dist}")

    # Check for negative-weight cycles
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            print("\nGraph contains a negative-weight cycle")
            return

    # Display shortest paths
    print("\nFinal shortest distances from source:")
    for i in range(vertices):
        print(f"Vertex {i}: {dist[i]}")

# User input section
V = int(input("Enter number of vertices: "))
E = int(input("Enter number of edges: "))
edges = []

print("Enter each edge in format: source destination weight (0-based index)")
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

source = int(input("Enter source vertex (0 to V-1): "))
bellman_ford(V, edges, source)
