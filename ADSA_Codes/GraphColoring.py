def is_safe(graph, color, v, c):
    """Check if it's safe to assign color c to vertex v."""
    for i in range(len(graph)):
        if graph[v][i] == 1 and color[i] == c:
            return False
    return True

def can_color_with_m(graph, m):
    """Check if the graph can be colored using m colors."""
    n = len(graph)
    color = [0] * n

    def solve(k):
        if k == n:
            return True
        for c in range(1, m + 1):
            if is_safe(graph, color, k, c):
                color[k] = c
                if solve(k + 1):
                    return True
                color[k] = 0
        return False

    if solve(0):
        return color
    else:
        return None

def graph_coloring_min_colors(graph):
    """Find the minimum number of colors needed to color the graph."""
    n = len(graph)
    for m in range(1, n + 1):
        result = can_color_with_m(graph, m)
        if result:
            print(f"\nMinimum colors needed: {m}")
            print("Assigned colors:")
            for i in range(n):
                print(f"Vertex {i + 1} ---> Color {result[i]}")
            return result
    print("No valid coloring found.")

def main():
    print("Graph Coloring using Backtracking (Minimum Colors)")
    n = int(input("Enter the number of vertices: "))
    print("Enter the adjacency matrix (row by row):")
    graph = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").strip().split()))
        if len(row) != n:
            print(f"Invalid row length. Please enter exactly {n} values.")
            return
        graph.append(row)

    graph_coloring_min_colors(graph)

if __name__ == "__main__":
    main()
