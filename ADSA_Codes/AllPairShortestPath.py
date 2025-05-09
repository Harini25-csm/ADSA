def floyd_warshall(graph, n):
    # Initialize the distance matrix
    dist = [[graph[i][j] for j in range(n)] for i in range(n)]

    # Initialize next node matrix
    next_node = [[j if graph[i][j] != float('inf') and i != j else -1 for j in range(n)] for i in range(n)]

    # Dynamic Programming approach
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    # Print result
    print("\nAll Pairs Shortest Paths Matrix:")
    for row in dist:
        print("\t".join("INF" if val == float('inf') else str(val) for val in row))

    return next_node, dist


def get_path(next_node, u, v):
    if next_node[u][v] == -1:
        return []

    path = [u + 1]  # Adjust for 1-based indexing
    while u != v:
        u = next_node[u][v]
        path.append(u + 1)
    return path


def main():
    n = int(input("Enter number of vertices: "))
    print("Enter adjacency matrix (use INF for no edge):")

    graph = []
    for i in range(n):
        row = input(f"Row {i+1}: ").split()
        graph.append([float('inf') if val.upper() == 'INF' else int(val) for val in row])

    next_node, dist = floyd_warshall(graph, n)

    print("\nShortest Paths:")
    for i in range(n):
        for j in range(n):
            if i != j:
                path = get_path(next_node, i, j)
                print(f"Path from {i + 1} to {j + 1}: {' -> '.join(map(str, path))}" if path else f"No path from {i + 1} to {j + 1}")


if __name__ == "__main__":
    main()
