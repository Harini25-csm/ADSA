# Function to solve Fractional Knapsack Problem using Greedy strategy
def fractional_knapsack(profits, weights, capacity):
    # Calculate profit-to-weight ratio and sort items in descending order
    ratio = sorted([(p / w, p, w) for p, w in zip(profits, weights)], reverse=True)
    
    total_profit = 0
    solution = [0] * len(profits)  # Solution vector
    
    for r, p, w in ratio:
        if capacity >= w:
            capacity -= w
            total_profit += p
            solution[weights.index(w)] = 1  # Mark full item taken
        else:
            fraction = capacity / w
            total_profit += p * fraction
            solution[weights.index(w)] = round(fraction, 2)  # Take fractional part
            break  # Knapsack is full
    
    # Output results
    print("\nSolution Vector:", solution)
    print(f"Total Profit: {total_profit:.2f}")

# Take input from user
def main():
    n = int(input("Enter number of items: "))
    profits, weights = [], []
    
    print("Enter profit and weight for each item:")
    for i in range(n):
        p, w = map(float, input(f"Item {i+1}: ").split())
        profits.append(p)
        weights.append(w)
    
    capacity = float(input("Enter knapsack capacity: "))
    fractional_knapsack(profits, weights, capacity)

if __name__ == "__main__":
    main()
