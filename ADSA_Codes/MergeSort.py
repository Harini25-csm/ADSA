import random
import time

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L, R = arr[:mid], arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

def measure_time(arr):
    start = time.time()
    merge_sort(arr)
    return time.time() - start

def generate_datasets(size):
    average_case = [random.randint(1, size) for _ in range(size)]
    best_case = sorted(average_case)
    worst_case = sorted(average_case, reverse=True)
    return average_case, best_case, worst_case

sizes = [1000, 2000, 5000, 10000, 20000, 50000]

print("\nMerge Sort Execution Time Analysis")
print("-----------------------------------")

for size in sizes:
    avg_case, best_case, worst_case = generate_datasets(size)
    print(f"\nInput Size: {size}")
    print(f" Average Case: {measure_time(avg_case.copy()):.5f} seconds")
    print(f" Best Case: {measure_time(best_case.copy()):.5f} seconds")
    print(f" Worst Case: {measure_time(worst_case.copy()):.5f} seconds")
    print("-----------------------------------")
