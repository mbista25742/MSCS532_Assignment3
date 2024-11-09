import random
import time
import sys

# Set the recursion limit to a higher value
sys.setrecursionlimit(2000)

# List of array sizes for the experiment
sizes = [100, 1000, 10000, 100000]

# Function to measure running time of a sorting function
def measure_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time

# Randomized QuickSort (random pivot)
def randomizedQuickSort(arr, low, high):
    if low < high:
        pivotIndex = partitionArrayRandomized(arr, low, high)
        randomizedQuickSort(arr, low, pivotIndex - 1)
        randomizedQuickSort(arr, pivotIndex + 1, high)

# Deterministic QuickSort (first element as pivot)
def deterministicQuickSort(arr, low, high):
    if low < high:
        pivotIndex = partitionArrayDeterministic(arr, low, high)
        deterministicQuickSort(arr, low, pivotIndex - 1)
        deterministicQuickSort(arr, pivotIndex + 1, high)

# Partition function for Randomized QuickSort
def partitionArrayRandomized(arr, low, high):
    pid = random.randint(low, high)  # Pick a random pivot
    arr[pid], arr[high] = arr[high], arr[pid]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Partition function for Deterministic QuickSort (first element as pivot)
def partitionArrayDeterministic(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

# Function to generate different types of arrays
def generate_arrays(size):
    random_arr = [random.randint(0, size) for _ in range(size)]
    sorted_arr = list(range(size))
    reversed_arr = sorted_arr[::-1]
    repeated_arr = [random.randint(0, size//2) for _ in range(size)]
    return random_arr, sorted_arr, reversed_arr, repeated_arr

# Function to compare running times of both sorting algorithms
def compare_sorting_times():
    for size in sizes:
        print(f"\nArray size: {size}")
        
        # Generate different types of arrays
        random_arr, sorted_arr, reversed_arr, repeated_arr = generate_arrays(size)
        
        # Measure time for Randomized QuickSort
        print("Randomized QuickSort:")
        print(f"Random Array: {measure_time(lambda arr: randomizedQuickSort(arr, 0, len(arr)-1), random_arr.copy())} seconds")
        print(f"Sorted Array: {measure_time(lambda arr: randomizedQuickSort(arr, 0, len(arr)-1), sorted_arr.copy())} seconds")
        print(f"Reverse Sorted Array: {measure_time(lambda arr: randomizedQuickSort(arr, 0, len(arr)-1), reversed_arr.copy())} seconds")
        print(f"Array with Repeated Elements: {measure_time(lambda arr: randomizedQuickSort(arr, 0, len(arr)-1), repeated_arr.copy())} seconds")
        
        # Measure time for Deterministic QuickSort
        print("\nDeterministic QuickSort:")
        print(f"Random Array: {measure_time(lambda arr: deterministicQuickSort(arr, 0, len(arr)-1), random_arr.copy())} seconds")
        print(f"Sorted Array: {measure_time(lambda arr: deterministicQuickSort(arr, 0, len(arr)-1), sorted_arr.copy())} seconds")
        print(f"Reverse Sorted Array: {measure_time(lambda arr: deterministicQuickSort(arr, 0, len(arr)-1), reversed_arr.copy())} seconds")
        print(f"Array with Repeated Elements: {measure_time(lambda arr: deterministicQuickSort(arr, 0, len(arr)-1), repeated_arr.copy())} seconds")

# Run the comparison
compare_sorting_times()
