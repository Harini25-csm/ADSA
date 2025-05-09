def sum_of_subsets(s, k, r, w, x, m, n):
    # Generate left child (include w[k])
    x[k] = 1
    if s + w[k] == m:
        # Subset found, print both the subset and solution vector
        print("Subset:", [w[i] for i in range(k + 1) if x[i] == 1])
        print("Solution vector:", x)
    elif s + w[k] + w[k + 1] <= m:
        sum_of_subsets(s + w[k], k + 1, r - w[k], w, x, m, n)
    
    # Generate right child (exclude w[k])
    if (s + r - w[k] >= m) and (s + w[k + 1] <= m):
        x[k] = 0
        sum_of_subsets(s, k + 1, r - w[k], w, x, m, n)

def main():
    n = int(input("Enter number of elements: "))
    w = list(map(int, input("Enter the elements (space-separated): ").split()))
    m = int(input("Enter the target sum: "))

    w.sort()  # Ensure weights are in non-decreasing order
    total = sum(w)
    x = [0] * n  # Solution vector

    print("Subsets that sum to", m, ":")
    if w[0] <= m and total >= m:
        sum_of_subsets(0, 0, total, w, x, m, n - 1)
    else:
        print("No solution")

if __name__ == "__main__":
    main()
