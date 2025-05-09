import sys

def min_key(key, mst_set, n):
    min_index = -1
    min_val = sys.maxsize

    for v in range(n):
        if not mst_set[v] and key[v] < min_val:
            min_val = key[v]
            min_index = v

    return min_index

def prim_mst(graph, n):
    key = [sys.maxsize] * n
    parent = [-1] * n
    mst_set = [False] * n
    key[0] = 0  

    for _ in range(n):
        u = min_key(key, mst_set, n)
        mst_set[u] = True

        for v in range(n):
            if graph[u][v] and not mst_set[v] and graph[u][v] < key[v]:
                key[v] = graph[u][v]
                parent[v] = u

    print("\nEdge \tWeight")
    total_cost = sum(graph[i][parent[i]] for i in range(1, n))
    for i in range(1, n):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")
    print(f"Total Cost of MST: {total_cost}")

def main():
    n = int(input("Enter number of vertices: "))
    print("Enter the adjacency matrix:")
    graph = [list(map(int, input().split())) for _ in range(n)]
    prim_mst(graph, n)

if __name__ == "__main__":
    main()
