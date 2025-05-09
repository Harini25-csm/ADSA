import itertools

def tsp_dp_with_path(cost_matrix):
    n = len(cost_matrix)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]
    
    dp[1][0] = 0  # Starting at city 0

    # Dynamic programming over subsets
    for mask in range(1 << n):
        for u in range(n):
            if mask & (1 << u):  # If u is in the subset
                for v in range(n):
                    if not (mask & (1 << v)):  # If v is not in the subset
                        new_mask = mask | (1 << v)
                        new_cost = dp[mask][u] + cost_matrix[u][v]
                        
                        if new_cost < dp[new_mask][v]:
                            dp[new_mask][v] = new_cost
                            parent[new_mask][v] = u

    # Find minimum cost to return to starting city
    full_mask = (1 << n) - 1
    min_cost = float('inf')
    last_city = -1

    for j in range(1, n):
        cost = dp[full_mask][j] + cost_matrix[j][0]
        if cost < min_cost:
            min_cost = cost
            last_city = j

    # Reconstruct the path
    path = []
    mask = full_mask
    current = last_city

    while current != -1:
        path.append(current)
        next_city = parent[mask][current]
        mask = mask ^ (1 << current)
        current = next_city

    path.append(0)  # Start city
    path.reverse()

    return min_cost, path

# Input
def read_input():
    n = int(input("Enter number of cities: "))
    print("Enter the cost matrix row by row (space-separated):")
    cost_matrix = []

    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError("Row must have exactly n values.")
        cost_matrix.append(row)

    return cost_matrix

# Main Execution
cost_matrix = read_input()
min_cost, path = tsp_dp_with_path(cost_matrix)

print(f"\nMinimum cost to complete the tour: {min_cost}")
print("Optimal tour path: " + " -> ".join(map(str, path)))
