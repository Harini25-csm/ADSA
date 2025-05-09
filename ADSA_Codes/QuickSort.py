import random
import time
import sys

sys.setrecursionlimit(10000)  # Increase recursion depth cautiously

def quick_sort(arr, low, high):
    if low < high:
        pi = random_partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def random_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Move pivot to end
    return partition(arr, low, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def measure_time(arr):
    start = time.time()
    quick_sort(arr, 0, len(arr) - 1)
    return time.time() - start

def generate_datasets(size):
    average_case = [random.randint(1, size) for _ in range(size)]
    best_case = average_case.copy()
    worst_case = sorted(average_case)
    return average_case, best_case, worst_case

sizes = [1000, 2000, 5000, 10000, 20000, 50000]

print("\nQuick Sort (Random Pivot) Execution Time Analysis")
print("-----------------------------------")

for size in sizes:
    avg_case, best_case, worst_case = generate_datasets(size)
    print(f"\nInput Size: {size}")
    print(f" Average Case: {measure_time(avg_case.copy()):.5f} seconds")
    print(f" Best Case: {measure_time(best_case.copy()):.5f} seconds")
    print(f" Worst Case: {measure_time(worst_case.copy()):.5f} seconds")
    print("-----------------------------------")
