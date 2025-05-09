class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u, root_v = self.find(u), self.find(v)
        if root_u != root_v:
            if self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            elif self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

def kruskal_mst(n, edges):
    ds = DisjointSet(n)
    edges.sort(key=lambda x: x[2])
    mst, total_cost = [], 0

    print("\nEdges in MST:")
    for u, v, weight in edges:
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight
            print(f"{u} - {v} \tWeight: {weight}")

    print(f"Total Cost of MST: {total_cost}")

def main():
    n = int(input("Enter number of vertices: "))
    e = int(input("Enter number of edges: "))
    print("Enter edges as: source destination weight")
    edges = [tuple(map(int, input().split())) for _ in range(e)]
    kruskal_mst(n, edges)

if __name__ == "__main__":
    main()
